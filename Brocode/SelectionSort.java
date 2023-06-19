package Brocode;

import java.util.*;

public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = { 10, 5, 3, 2, 4, 8, 1, 6, 9, 7 };

        System.out.println("Before sorting:" + Arrays.toString(arr));
        System.out.println("After sorting:" + Arrays.toString(selectionSort(arr)));
    }

    private static int[] selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int min = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[min] > arr[j]) {
                    min = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }

        return arr;
    }
}
