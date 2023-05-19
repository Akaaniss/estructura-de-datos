import 'dart:io';
import 'dart:math';

void main() {
  // Lista por elementos
  List<int> lista1 = [14, 2, 5, 3, 9];
  print("Primera lista: $lista1");

  // Lista por teclado
  List<int> lista2 = [];
  for (int i = 0; i < 5; i++) {
    stdout.write("Ingrese el elemento ${i + 1}: ");
    int elemento = int.parse(stdin.readLineSync()!);
    lista2.add(elemento);
  }
  print("Segunda lista: $lista2");

  // Números negativos
  List<int> lista3 = [];
  Random random = Random();
  for (int i = 0; i < 5; i++) {
    int numeroAleatorio = random.nextInt(11) - 15;
    lista3.add(numeroAleatorio);
  }
  print("Tercera lista: $lista3");

  // restar
  List<int> resultado = [];
  for (int i = 0; i < 5; i++) {
    int resta = lista1[i] - lista2[i];
    int suma = resta + lista3[i];
    resultado.add(suma);
  }
  print("Resultado: $resultado");

  resultado.insert(0, 17);
  resultado.insert(1, 24);
  print("Resultado con inserciones: $resultado");

  // Orden descendente
  resultado.sort((a, b) => b.compareTo(a));
  print("Resultado ordenado de forma descendente: $resultado");
}
