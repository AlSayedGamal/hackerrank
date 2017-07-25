object Solution {

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        val t = sc.nextInt();
        var a0: Int = 0;
        val left = Map('(' -> ')','{' -> '}', '[' -> ']')
        val right = Map(')' -> '(','}' -> '{', ']' -> '[')
        while(a0 < t){
            var expression = sc.next();
            a0+=1;
            go(expression)
        }
        def go(exp: String): Unit = {
            val s = new scala.collection.mutable.Stack[Char]
            var flag =
                if(exp.length % 2 != 0) false
                else exp.forall(c =>
                    if(left.isDefinedAt(c))  {s.push(c); true}
                    else{
                        if(s.isEmpty) false
                        else if(right(c) == s.pop) { true }
                        else false
                    }
                )
            if(s.size > 0) flag = false
            if(flag) println("YES") else println("NO")
        }
    }
}
