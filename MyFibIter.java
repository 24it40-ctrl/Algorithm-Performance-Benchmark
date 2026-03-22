import java.util.Scanner;
import java.math.BigInteger; // Bade numbers ki 'Freedom' ke liye

public class MyFibIter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n (Iterative): ");

        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            
            long start = System.nanoTime();
            
            BigInteger a = BigInteger.ZERO;
            BigInteger b = BigInteger.ONE;
            
            System.out.print("Full Series: ");
            for (int i = 0; i <= n; i++) {
                System.out.print(a + " ");
                BigInteger next = a.add(b);
                a = b;
                b = next;
            }
            
            long end = System.nanoTime();
            System.out.println("\nTime Taken: " + (end - start) + " ns");
        }
    }
}