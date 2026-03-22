import java.util.Scanner;

public class MyFibRec {
    public static long getFib(int n) {
        if (n <= 1) return n;
        return getFib(n - 1) + getFib(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n (Recursive): ");
        
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            if (n < 0) {
                System.out.println("Invalid! Positive number chahiye.");
                return;
            }

            long start = System.nanoTime();
            long result = getFib(n);
            long end = System.nanoTime();

            System.out.println("Result (n=" + n + "): " + result);
            System.out.println("Time: " + (end - start) + " ns");
            System.out.println("Digits: " + String.valueOf(result).length());
        }
    }
}