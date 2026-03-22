import java.util.Scanner;

public class SDSI {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        String s = sc.next();
        if(s.matches("\\d+")) {
            long start = System.nanoTime();
            while (s.length() > 1) {
                long sum = 0;
                for (char c : s.toCharArray()) sum += (c - '0');
                s = String.valueOf(sum);
            }
            long end = System.nanoTime();
            System.out.println("Result: " + s + " | Time: " + (end-start)/1000000.0 + " ms");
        }
    }
}
