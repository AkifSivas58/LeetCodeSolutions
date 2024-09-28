import java.util.LinkedList;
class MyCircularDeque {
    private LinkedList<Integer> deque = new LinkedList<Integer>();
    private int k;
    public MyCircularDeque(int k) {
        this.k = k;
    }
    
    public boolean insertFront(int value) {
        if (deque.size() < k){
            deque.addFirst(value);
            return true;
        }
        else{
            return false;
        }
    }
    
    public boolean insertLast(int value) {
        if (deque.size() < k){
            deque.addLast(value);
            return true;
        }
        else{
            return false;
        }
    }
    
    public boolean deleteFront() {
        if (deque.size() > 0){
            deque.removeFirst();
            return true;
        }
        else{
            return false;
        }
    }
    
    public boolean deleteLast() {
        if (deque.size() > 0){
            deque.removeLast();
            return true;
        }
        else{
            return false;
        }
    }
    
    public int getFront() {
        if (deque.size() > 0){
            return deque.get(0);
        }
        return -1;
    }
    
    public int getRear() {
        if (deque.size() > 0){
            return deque.get(deque.size() -1);
        }
        return -1;
    }
    
    public boolean isEmpty() {
        if (deque.size() > 0){
            return false;
        }
        return true;
    }
    
    public boolean isFull() {
        if (deque.size() == k){
            return true;
        }
        return false;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */