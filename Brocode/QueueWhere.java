package Brocode;

import java.util.*;

public class QueueWhere {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<String>();

        System.out.println(queue.isEmpty());

        queue.offer("A");
        queue.offer("B");
        queue.offer("C");
        queue.offer("D");

        System.out.println(queue.peek());
        System.out.println(queue.contains("A"));

        queue.poll();

        System.out.println(queue.isEmpty());
        System.out.println(queue.size());
        System.out.println(queue);
    }
}
