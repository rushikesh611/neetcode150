package Brocode;

import java.util.*;

public class PriorityQueueWhere {
    public static void main(String[] args) {
        Queue<String> queue = new PriorityQueue<>(Collections.reverseOrder());

        queue.offer("C");
        queue.offer("B");
        queue.offer("A");
        queue.offer("F");
        queue.offer("D");

        while (!queue.isEmpty()) {
            System.out.println(queue.poll());
        }

    }
}
