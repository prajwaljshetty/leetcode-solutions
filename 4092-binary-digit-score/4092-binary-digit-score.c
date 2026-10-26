int countBits(int n){
    int count = 0;
    while(n > 0){
        if(n & 1) count++;
        n >>= 1;
    }
    return count;
}

int calculateScore(int a, int b) {
    int bitA = countBits(a) , bitB = countBits(b);
    return bitA >= bitB ? bitA * bitB : (bitA != 0 ? ((int) bitB / bitA) : 0);
}