package Brocode;

public class MergeSort {
    public static void main(String[] args) {
        int[] arr = { 5, 4, 3, 2, 1, 7, 6, 8, 9, 10 };

        mergeSort(arr);

        for (int i : arr) {
            System.out.print(i + " ");
        }
    }

    private static void mergeSort(int[] arr) {
        int length = arr.length;

        if (length <= 1) {
            return;
        }

        int mid = length / 2;

        int[] leftArray = new int[mid];
        int[] rightArray = new int[length - mid];

        int i = 0;
        int j = 0;

        for (; i < length; i++) {
            if (i < mid) {
                leftArray[i] = arr[i];
            } else {
                rightArray[j] = arr[i];
                j++;
            }
        }
        mergeSort(leftArray);
        mergeSort(rightArray);
        merge(leftArray, rightArray, arr);

    }

    private static void merge(int[] leftArray, int[] rightArray, int[] arr) {
        int leftLength = arr.length / 2;
        int rightLength = arr.length - leftLength;
        int i = 0, l = 0, r = 0;

        // check conditions for merging
        while (l < leftLength && r < rightLength) {
            if (leftArray[l] < rightArray[r]) {
                arr[i] = leftArray[l];
                i++;
                l++;
            } else {
                arr[i] = rightArray[r];
                i++;
                r++;
            }
        }

        while (l < leftLength) {
            arr[i] = leftArray[l];
            i++;
            l++;
        }

        while (r < rightLength) {
            arr[i] = rightArray[r];
            i++;
            r++;
        }
    }
}
