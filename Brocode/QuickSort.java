package Brocode;

public class QuickSort {
    public static void main(String[] args) {
        int[] arr = { 5, 4, 3, 2, 1, 7, 6, 8, 9, 10 };

        quickSort(arr, 0, arr.length - 1);

        for (int i : arr) {
            System.out.print(i + " ");
        }
    }

    private static void quickSort(int[] arr, int startIdx, int endIdx) {
        if (endIdx <= startIdx) {
            return;
        }

        int pivot = partition(arr, startIdx, endIdx);
        quickSort(arr, startIdx, pivot - 1);
        quickSort(arr, pivot + 1, endIdx);

    }

    private static int partition(int[] arr, int startIdx, int endIdx) {
        int pivot = arr[endIdx];
        int i = startIdx - 1;

        for (int j = startIdx; j <= endIdx - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        i++;
        int temp = arr[i];
        arr[i] = arr[endIdx];
        arr[endIdx] = temp;
        return i;
    }
}
