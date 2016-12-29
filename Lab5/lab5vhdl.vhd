
library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity and_or_xor is
	port(
		a,b: in std_logic;
		in1, in2, y_and, y_or, y_xor: out std_logic
	);
end and_or_xor;

architecture arch1 of and_or_xor is
begin
	in1 <= a;
	in2 <= b;
	
	y_and <= not ((not a) and (not b));
	y_or <= not ((not a) or (not b));
	y_xor <= not ((not a) xor (not b));
end arch1;