object Solution {
    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var a = sc.next();
        var b = sc.next();
        val r = new Array[Int](26)
        for(c <- a) r(c - 97) += 1
        for(c <- b) r(c - 97) -= 1
        println(r.reduce(Math.abs(_) + Math.abs(_)))
    }
}
