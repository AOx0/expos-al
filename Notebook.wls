#!/usr/bin/env wolframscript
(* ::Package:: *)

Sw[mat_, r_] := Module[{tem, res=mat}, 
	tem = res[[r[[2]]]] ;
	res[[r[[2]]]]= res[[r[[1]]]] ;
	res[[r[[1]]]]= tem;
	res
];

Rp[mat_, r_, op_] := Module[{tem, res=mat}, 
	res[[r[[2]]]] = op mat[[r[[1]]]] + mat[[r[[2]]]] ;
	res
];


mat=({
 {1, 2, 4, 1, -1, 1},
 {2, 4, 8, 3, -4, 2},
 {1, 3, 7, 0, 3, -2}
});

mat = Rp[mat, {1, 2}, -2];
mat = Rp[mat, {1, 3}, -1];
mat = Sw[mat, {2,3}];
MatrixForm@mat
mat = Rp[mat, {3, 2}, 1];
mat = Rp[mat, {3, 1}, -1];
mat = Rp[mat, {2, 1}, -2];
MatrixForm@mat



