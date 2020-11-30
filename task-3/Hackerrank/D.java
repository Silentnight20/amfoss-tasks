import java.util.*; 
public class pattern { 
    public static void main(String[] args) 
    { 
        int n;

        do {
            Scanner sc = new Scanner(System.in); 
            n = sc.nextInt();
        }while(n <= 1 || n >= 30 || n%2 == 0);

        int rows = n/2;
  
        for (int i = 1; i <= rows; i++) { 
  
            for (int j = rows; j >= i; j--) { 
                System.out.print("*"); 
            } 

            for (int j = 1; j <= 2*i - 1; j++) { 
                System.out.print("D"); 
            } 
            
            for (int j = rows; j >= i; j--) { 
                System.out.print("*"); 
            } 
            System.out.println(); 
        } 
        for (int i = 0; i < n; i++) {
            System.out.print("D");
        }
        System.out.println();

        for (int i = rows; i > 0; i--) {
            for (int j = rows; j >= i; j--) {
                System.out.print("*");
            }
            for (int j = 0; j < (i * 2 - 1); j++) {
                System.out.print("D");
            }
            for (int j = rows; j >= i; j--) {
                System.out.print("*");
            }
            System.out.println();
        }                       
    } 
} 