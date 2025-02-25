#include <stdio.h>

struct sll{
    int data;
    struct sll *next;
};

typedef struct sll node;

node *start = NULL;

node *craete(){
    node *nn = (node*) malloc (sizeof(node));
    printf("Enter the data: ");
    scanf("%d",&nn->data);
    nn->next = NULL;
    return nn;
}

void insert_front(){
    node *nn = create();
    if (start == NULL){
        start=nn;
    }
    else{
        nn->next=start;
        start=nn;
    }
}

void insert_rear(){
    node *nn=create(), *temp=start;
    while(temp!=`)
}