/*
$225. Implement Stack using Queues
*/

class MyStack {
public:
    queue<int> main_queue, tmp_queue;

    // Initialize our data structure here.
    MyStack() {
    }

    // Push element x onto stack.
    void push(int x) {
        while (!main_queue.empty()) {
            tmp_queue.push(main_queue.front());
            main_queue.pop();
        }
        main_queue.push(x);
        while (!tmp_queue.empty()) {
            main_queue.push(tmp_queue.front());
            tmp_queue.pop();
        }
    }

    int pop() {
        int val = main_queue.front();
        main_queue.pop();
        return val;
    }

    int top() {
        return main_queue.front();
    }

    bool empty() {
        return main_queue.empty();
    }
};