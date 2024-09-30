import java.util.ArrayList;
class CustomStack {
    private ArrayList<Integer> arr;
    private int maxSize;
    public CustomStack(int maxSize) {
        this.maxSize = maxSize;
        this.arr = new ArrayList<Integer>();
    }
    
    public void push(int x) {
        if (arr.size() < maxSize){
            arr.add(x);
        }
    }
    
    public int pop() {
        int val = -1;
        if (arr.size() > 0){
            val = arr.get(arr.size() -1);
            arr.remove(arr.size()-1);
        } 
        
        return val;
    }
    
    public void increment(int k, int val) {
        for (int i = 0; i < arr.size(); i++){
            if (i > k-1){
                break;
            }
            arr.set(i, arr.get(i) + val);
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */