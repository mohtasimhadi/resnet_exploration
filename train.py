import torch
import torch.nn as nn
import torch.optim as optim
from utils.log_texts import CYAN, LOG, RESET, SUCCESS
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def train(model, train_loader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item() * inputs.size(0)
    
    epoch_loss = running_loss / len(train_loader.dataset)
    return epoch_loss

def evaluate(model, test_loader, device):
    model.eval()
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    
    accuracy = accuracy_score(all_labels, all_preds)
    precision = precision_score(all_labels, all_preds, average='weighted')
    recall = recall_score(all_labels, all_preds, average='weighted')
    f1 = f1_score(all_labels, all_preds, average='weighted')
    return accuracy, precision, recall, f1

def evaluate_errors(model, test_loader, device):
    model.eval()
    top1_correct = 0
    top5_correct = 0
    total_samples = 0

    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, preds = torch.topk(outputs, k=5, dim=1)
            total_samples += labels.size(0)
        
            top1_correct += (preds[:, 0] == labels).sum().item()

            top5_correct += torch.tensor([label in pred for label, pred in zip(labels, preds)]).sum().item()

    top1_accuracy = top1_correct / total_samples
    top5_accuracy = top5_correct / total_samples

    return 1 - top1_accuracy, 1 - top5_accuracy 


def run_training(model_fn, train_loader, test_loader, num_classes, num_epochs=10):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = model_fn(num_classes).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(num_epochs):
        train_loss = train(model, train_loader, criterion, optimizer, device)
        accuracy, precision, recall, f1 = evaluate(model, test_loader, device)
        
        print(f"{LOG}{CYAN}Epoch {epoch+1}/{num_epochs}{RESET}\n\t\tLoss: {train_loss:.4f}\n\t\tAccuracy: {accuracy:.4f}\n\t\t"
              f"Precision: {precision:.4f}\n\t\tRecall: {recall:.4f}\n\t\tF1-Score: {f1:.4f}")
    
    final_top1_err, final_top5_err = evaluate_errors(model, test_loader, device)
    print(f"{SUCCESS}Training complete!\n\t\tFinal Top-1 Error: {final_top1_err:.4f}\n\t\tFinal Top-5 Error: {final_top5_err:.4f}")