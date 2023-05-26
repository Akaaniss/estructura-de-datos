import 'dart:io';
import 'dart:math';

void main() { 
  List<int>lista1= listaAleatoria(10,10,20);
  List<int>lista2= listaAleatoria(10,10,20);
  List<int>lista3= listaporTeclado(5);

  List<int> concadenada=[...lista1,...lista2,...lista3];
  double prom = calcularProm(concadenada);

  concadenada.sort();

  print('Lista 1: $lista1');
  print('Lista 2: $lista2');
  print('Lista 3: $lista3');
  print('Lista concadenada: $concadenada');
  print('Promedio: $prom');
}

List<int>listaAleatoria(int cantidad, int rangoMinimo, int rangoMaximo) { 
  Random random = Random();
  List<int>lista=[];

  for(int i=0; i< cantidad; i++) { 
    int elemento = random.nextInt(rangoMaximo-rangoMinimo +1)+rangoMinimo;
    lista.add(elemento);
  }
  return lista;
}

List<int>listaporTeclado(int cantidad) {
  List<int>lista=[];
  print('ingrese $cantidad de elementos enteros:');

  for(int i=0; i<cantidad;i++) {
    int elemento =int.parse(stdin.readLineSync()!);
    lista.add(elemento);
  }
  return lista;
}

double calcularProm(List<int>lista) {
  int suma= lista.reduce((a,b)=> a+b);
  return suma/lista.length;
}