import java.util.Scanner;

public class MyFibFormula {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n (Formula): ");

        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            
            long start = System.nanoTime();
            
            // Math formula: phi^n / sqrt(5)
            double root5 = Math.sqrt(5);
            double phi = (1 + root5) / 2;
            long res = Math.round(Math.pow(phi, n) / root5);
            
            long end = System.nanoTime();

            System.out.println("Formula Result: " + res);
            System.out.println("Execution Speed: " + (end - start) + " ns");
        }
    }
}