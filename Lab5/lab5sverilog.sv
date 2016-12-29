
module project(
	input logic a,b,
	output logic in1, in2, y_and, y_or, y_xor
);

	assign in1=a;
	assign in2=b;
	assign y_and = ~(~a & ~b );
	assign y_or = ~(~a || ~b);
	assign y_xor = ~( ~a ^ ~b );
	
endmodule