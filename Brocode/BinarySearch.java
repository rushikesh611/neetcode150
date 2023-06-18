package Brocode;

import java.util.Arrays;

public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = { 3, 6, 1, 8, 9, 2, 4, 7, 5 };

        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));

        // int index = Arrays.binarySearch(arr, 7);
        int index = binarySearch(arr, 5);

        if (index != -1) {
            System.out.println("Element found at index " + index);
        } else {
            System.out.println("Element not found");
        }
    }

    private static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            int value = arr[mid];

            if (value < target) {
                left = mid + 1;
            } else if (value > target) {
                right = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
