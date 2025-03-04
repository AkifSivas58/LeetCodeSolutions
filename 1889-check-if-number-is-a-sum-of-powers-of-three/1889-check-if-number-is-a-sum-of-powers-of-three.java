class Solution {
    public boolean checkPowersOfThree(int n) {
        while(n > 1){
            int modi = n % 3;
            n /= 3 ;
            if(modi == 2){
                return false;
            }
        }
        return true;
    }
}