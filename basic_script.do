#apparently, it just starts like this


#now, I know semicolon is not necessary, but why take the risk??
puts "Hello World!, this is Supreeth";


#now these are values
set num_a 2;
set num_b 3;
set num_d 4;


#now strings

set str1 "4";
set str2 5;
set str3 Hello;
set var1 World;

#Now I do basic arithmetic with num_a and num_b


puts "now some basic arithmetics";
puts "---------------------------";
puts [expr $num_a + $num_b]; #add
puts [expr $num_a - $num_b]; #neg_sub
puts [expr $num_b - $num_a]; #subtract
puts [expr $num_a * $num_b]; #multiply
puts [expr $num_a / $num_b]; #div 1
puts [expr $num_b / $num_a]; #div 2

#string concatenation type now



puts "now the string concatenation";
puts "$str3 World, this is $str1 and $str2"; #expected line "Hello World, this is 4 and 5"

#if and error catching


puts "now if compares and div by zero errors";
if {$num_b > $num_a} {
    set num_c 0;

    if {[catch {expr $num_b / $num_c} error_zero_div]} {

        puts "error happened as expected";
        puts $error_zero_div;
    }
}

#function 
puts "now this is the function"
proc say_hello {name} {
    puts "Hello $name";
}

#invoke function
say_hello World;

#for loop to count from 0 -> 10

puts "now this is the for loop";
for {set i 0} {$i < 10} {incr i} {

    puts $i;
}

#for loop to count from 0 -> 10, but now, incr by 2


puts "for loop incr by 2";


#I know this might be wrong
for {set i 0} {$i < 10} {incr i 2} {
    puts $i;

}


#foreach loop

puts "now the foreach loop";

set list1 {num_a num_b num_d};

foreach item $list1 {
    puts $item;
}


puts "end of program";

#end



