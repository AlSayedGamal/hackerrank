object Solution {

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var m = sc.nextInt();
        var n = sc.nextInt();
        val magazine = new Array[String](m);
        for(magazine_i <- 0 to m-1) {
           magazine(magazine_i) = sc.next();
        }
        val ransom = new Array[String](n);
        for(ransom_i <- 0 to n-1) {
           ransom(ransom_i) = sc.next();
        }

        var mag = magazine.foldLeft(Map.empty[String, Int])((z,b) => if(z.isDefinedAt(b)) z.updated(b, z(b) +1) else z ++ Map(b -> 1))
        val flag = ransom.forall(x => if(mag.isDefinedAt(x) && mag(x) > 0) {mag = mag.updated(x, mag(x)-1 );true} else false)
        if(flag) println("Yes") else println("No")
    }
}
