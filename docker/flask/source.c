#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void main(){
  setuid(222);
  printf("Poisoning is a bad thing!");
  system("cat research.txt");
}
