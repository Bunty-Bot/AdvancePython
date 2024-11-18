import numpy as np
import matplotlib.pyplot as plt

class biodata:
  def __init__(self, name, data):
    self.name = name
    self.data = data
  from abc import abstractmethod
  @abstractmethod
  def analyse(self):
    pass
  @abstractmethod
  def visualise(self):
    pass
  @abstractmethod
  def summary(self):
    pass

class ProteinSequences(biodata):
  def __init__(self, name, sequence):
    super().__init__(name, sequence)
    self.sequence = sequence

  def analyse(self):
    return ("Length", len(self.sequence), "Unique_amino_acids: ", len(set(self.sequence)))

  def visualise(self):
    amino_acid_counts = {aa: self.sequence.count(aa) for aa in set(self.sequence)}
    plt.bar(amino_acid_counts.keys(), amino_acid_counts.values())
    plt.xlabel('Amino Acid')
    plt.ylabel('Count')
    plt.title(f'Amino Acid Distribution for {self.name}')
    plt.show()

  def summary(self):
    amino_acid_counts = {aa: self.sequence.count(aa) for aa in set(self.sequence)}
    total_amino_acids = len(self.sequence)
    unique_amino_acids = len(amino_acid_counts)
    return {"Name": self.name, "Total_amino_acids": total_amino_acids, "Unique_amino_acids": unique_amino_acids, "Amino Acid Counts": amino_acid_counts}

class GeneExpression(biodata):
  def __init__(self, name, expression_levels):
    super().__init__(name, expression_levels)
    self.expression_levels = expression_levels

  def analyse(self):
    return ("Mean", np.mean(self.expression_levels), "Median", np.median(self.expression_levels), "Standard_deviation", np.std(self.expression_levels))

  def visualise(self):
    plt.plot(self.expression_levels)
    plt.ylabel('Expression Level')
    plt.xlabel('Time')
    plt.title(f'Gene Expression Distribution for {self.name}')
    plt.show()

  def summary(self):
    return {"Name": self.name, "Mean": np.mean(self.expression_levels), "Median": np.median(self.expression_levels), "Standard_deviation": np.std(self.expression_levels)}

while True:
  print("1. Analyse Protein Sequences")
  print("2. Analyse Gene Expression")
  print("3. Show summary statistics")
  print("4. Exit")

  choice = input("Enter your choice: ")

  if choice == '1':
    name = input("Enter the name of the protein sequence: ")
    sequence = input("Enter the protein sequence: ")
    protein_sequence = ProteinSequences(name, sequence)
    print(protein_sequence.analyse())


  elif choice == '2':
    name = input("Enter the name of the gene: ")
    expression_levels = input("Enter the gene expression levels (comma-separated): ")
    expression_levels = [float(x) for x in expression_levels.split(',')]
    gene_expression = GeneExpression(name, expression_levels)
    print(gene_expression.analyse())


  elif choice == '3':
    name = input("Enter the type of data for summary (Protein/Gene): ").lower()
    if name == 'protein':
      name = input("Enter the name of the protein sequence: ")
      sequence = input("Enter the protein sequence: ")
      protein_sequence = ProteinSequences(name, sequence)
      print(protein_sequence.summary())
      protein_sequence.visualise()
    elif name == 'gene':
      name = input("Enter the name of the gene: ")
      expression_levels_str = input("Enter the gene expression levels (comma-separated): ")
      expression_levels = [float(x) for x in expression_levels_str.split(',')]
      gene_expression = GeneExpression(name, expression_levels)
      print(gene_expression.summary())
      gene_expression.visualise()

    else:
      print("Invalid choice. Please try again.")
  elif choice == '4':
    print("Exiting the program. Thank you for using my code!!")
    break
  else:
    print("Invalid choice. Please try again.")
