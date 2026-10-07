class Solution {
  List<int> decode(List<int> encoded, int first) {
    List<int>  decoded = [first];
    int xor = first;
    for( int i = 0 ; i < encoded.length ; i++){
        xor ^= encoded[i];
        decoded.add(xor);
    }
    return decoded;
  }
}