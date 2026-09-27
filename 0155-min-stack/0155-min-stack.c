#include <limits.h>

typedef struct {
    int *stack , *min ;
    int top , capacity;
} MinStack;


MinStack* minStackCreate() {
    MinStack *obj = malloc( sizeof( MinStack ) );
    obj->capacity = 10;
    obj->min = malloc(obj->capacity * sizeof( int ));
    obj->stack = malloc(obj->capacity * sizeof( int ) );
    obj->top = -1;
    return obj;
}

void minStackPush(MinStack* obj, int value) {
    if( obj->top ==  obj->capacity - 1 ){
        obj->capacity += 10;
        obj->stack = realloc( obj-> stack , obj->capacity * sizeof(int) );
        obj->min = realloc( obj-> min , obj->capacity * sizeof(int) );
    }
    obj->stack[++obj->top] = value;
    if( obj->top - 1 >= 0 && obj->min[obj->top - 1] < value ) {
        obj->min[obj->top] = obj->min[obj->top - 1];
    }else{
        obj->min[obj->top] = value;
    }
}

void minStackPop(MinStack* obj) {
    obj->top--;
}

int minStackTop(MinStack* obj) {
    return obj->stack[obj->top];
}

int minStackGetMin(MinStack* obj) {
    return obj->min[obj->top];
}

void minStackFree(MinStack* obj) {
    free(obj->stack);
    free(obj->min);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, value);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/