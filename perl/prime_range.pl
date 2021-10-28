#!/usr/bin/perl

print "Find primes from: ";
$o = <>;
print "to: ";
$e = <>;

for($i=$o; $i<=$e; $i++){
$p=0;
    for($j=1; $j<=$i; $j++){
        if($i % $j==0){

            $prime_[$p] = "$j";
            $p++;
        }
        if ($prime_[1] == $i){
            print "$i is prime";
            print "\n";
        }
    }

}
