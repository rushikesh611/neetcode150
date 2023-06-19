package Brocode;

import java.util.*;

public class BubbleSort {
    public static void main(String[] args) {
        int[] arr = { 1, 5, 3, 2, 4, 8, 10, 6, 9, 7 };

        System.out.println("Before sorting:" + Arrays.toString(arr));
        System.out.println("After sorting:" + Arrays.toString(bubbleSort(arr)));
    }

    private static int[] bubbleSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        return arr;
    }
}
