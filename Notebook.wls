#!/usr/bin/env wolframscript
(* ::Package:: *)

Sw[mat_, r_] := Module[{tem, res=mat}, 
	tem = res[[r[[2]]]] ;
	res[[r[[2]]]]= res[[r[[1]]]] ;
	res[[r[[1]]]]= tem;
	Simplify[res]
];

Rp[mat_, r_, op_] := Module[{tem, res=mat}, 
	res[[r[[2]]]] = op mat[[r[[1]]]] + mat[[r[[2]]]] ;
	Simplify[res]
];

Rd[mat_, r_, op_] := Module[{tem, res=mat}, 
	res[[r]] = mat[[r]]/op;
	Simplify[res]
];


mat=({
 {1, 2, 4, 1, -1, 1},
 {2, 4, 8, 3, -4, 2},
 {1, 3, 7, 0, 3, -2}
});

(* Gauss *)
mat = Rp[mat, {1, 2}, -2];
MatrixForm@mat
mat = Rp[mat, {1, 3}, -1];
MatrixForm@mat
mat = Sw[mat, {2,3}];
MatrixForm@mat

(* Gauss-Jordan *)
mat = Rp[mat, {3, 2}, 1];
MatrixForm@mat
mat = Rp[mat, {3, 1}, -1];
MatrixForm@mat
mat = Rp[mat, {2, 1}, -2];
MatrixForm@mat


mat=({
 {1, 2, 0, p1},
 {2, 1, 1, p2},
 {2, -1, 1, p3},
 {1, 2, 2, p4}
});

(* Gauss *)
mat = Rp[mat, {1, 2}, -2];
MatrixForm@mat
mat = Rp[mat, {1, 3}, -2];
MatrixForm@mat
mat = Rp[mat, {1, 4}, -1];
MatrixForm@mat

(* Gauss  1/2*)
mat = Rd[mat, 2, -3];
MatrixForm@mat
mat = Rp[mat, {2, 3}, 5];
MatrixForm@mat
mat = Rd[mat, 3, -2/3];
MatrixForm@mat
mat = Rp[mat, {3, 4}, -2];
MatrixForm@mat

(* Jordan *)
mat = Rp[mat, {3, 2}, 1/3];
MatrixForm@mat
mat = Rp[mat, {2, 1}, -2];
MatrixForm@mat


MatrixForm@RowReduce[{
 {1, 2, 0},
 {2, 1, 1},
 {2, -1, 1},
 {1, 2, 2}
}]


Simplify[p1-2 (1/3 (2 p1-p2)+1/2 (2 p1-5/3 (2 p1-p2)-p3))]
