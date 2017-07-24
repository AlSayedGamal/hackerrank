object Solution {

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var a = sc.next();
        var b = sc.next();
        val s1 = a.foldLeft(Map.empty[Char, Int])((z,b) => if(z.isDefinedAt(b)) z.updated(b, z(b)+1) else z ++ Map(b -> 1))
        val s2 = b.foldLeft(Map.empty[Char, Int])((z,b) => if(z.isDefinedAt(b)) z.updated(b, z(b)+1) else z ++ Map(b -> 1))
        val r = s2.foldLeft(s1)((z, b) => if(z.isDefinedAt(b._1)) z.updated(b._1, Math.abs(z(b._1)-b._2)) else z ++ Map(b._1 -> b._2) ).foldLeft(0)((z,b) => z + b._2)
        println(r)

    }

}
