object Solution {

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var n = sc.nextInt();
        var k = sc.nextInt();
        var a = new Array[Int](n);
        for(a_i <- 0 to n-1) {
           a(a_i) = sc.nextInt();
        }
        
        val rCount = k % n
        val preResult = a.splitAt(rCount)
        (preResult._2 ++ preResult._1).map(e => print(s"$e "))
    }
}
