object Solution {

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in)
        val n = sc.nextInt()
        val k = sc.nextInt()
        val a = new Array[Int](n)
        for(a_i <- 0 to n-1) {
           a(a_i) = sc.nextInt()
        }
        val b = new Array[Int](n)
        for(i <- 0 to n-1) {
            val n = i - k;
            if(n >= 0) b(n)=a(i) else b(a.length+n)=a(i)
        }
        b.foreach(c => print(c + " "))
    }
}
