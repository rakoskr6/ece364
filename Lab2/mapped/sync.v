/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : K-2015.06-SP1
// Date      : Mon Sep  7 21:39:49 2015
/////////////////////////////////////////////////////////////


module sync ( clk, n_rst, async_in, sync_out );
  input clk, n_rst, async_in;
  output sync_out;


  DFFSR sync_out_reg ( .D(async_in), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        sync_out) );
endmodule

