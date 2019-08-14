//////////////////////////////////////////////////////////////////////////
//KANSI

difference(){
union(){
difference(){
difference(){
	sphere(d = 120, $fn = 100);
	sphere(d = 105, $fn = 50);
}
	union(){
	translate([0,0,-60])cube([120,120,120], center = true );
	translate([0,0,49])cylinder(h=11, d=3, $fn=25);
	translate([0,0,49])cylinder(h=8.5, d=7.5, $fn=25);
	translate([0,0,5])cube([2,6,5], center = true );
		
		
		
	for (a = [0:120:240]){
		rotate([0,0,a])translate([0,42.5,27.5])rotate([-56.5,0,0])union(){
			hull(){
			cylinder(h=3, d=15, $fn=35);
			translate([0,0,6])cylinder(h=3, d=24, $fn=35);
			}
			translate([0,0,5])cylinder(h=25, d=30, $fn=35);
		}
		rotate([0,0,a])translate([0,28,45])rotate([-32.5,0,0])union(){
			cube([14,9,10], center = true );
			translate([0,0,5])cube([6,6,5], center = true );
		}
		}	
}
}
	for (a = [0:120:240]){
		rotate([0,0,a])translate([0,-12.5,27.75])difference(){
			union(){
			translate([0,0,0.25])cylinder(h=29, d=7, $fn=35);
			hull(){
			translate([0,0,4])cylinder(h=24, d=7, $fn=35);
			translate([7.5,-25,10])cylinder(h=6, d=5, $fn=35);
			translate([-7.5,-25,10])cylinder(h=6, d=5, $fn=35);
			}
			}
			union(){
			cylinder(h=7.5, d=3, $fn=35);
			translate([0,0,7.5])hull(){
			translate([0,-1,0])cylinder(h=3.5, d=4.5, $fn=35);	
			translate([0,6,0])cylinder(h=3.5, d=4.5, $fn=35);	
			}
			}
		}
		rotate([0,0,a])translate([0,-50,4.15])rotate([0,0,-90])difference(){
		union(){	
		hull(){
		union(){
		translate([4,5,0])cylinder(h=4, d=3, $fn=35);
		translate([-2,5,0])cylinder(h=4, d=3, $fn=35);		
		translate([4,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-2,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-5,2.5,0])cylinder(h=4, d=5, $fn=35);
		translate([-5,-2.5,0])cylinder(h=4, d=5, $fn=35);
		}
		translate([0,0,5])union(){
		translate([4,5,0])cylinder(h=4, d=3, $fn=35);
		translate([-2,5,0])cylinder(h=4, d=3, $fn=35);		
		translate([4,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-2,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-5,2.5,0])cylinder(h=4, d=5, $fn=35);
		translate([-5,-2.5,0])cylinder(h=4, d=5, $fn=35);	
		}
		translate([0,0,20])union(){
		translate([1,5,0])cylinder(h=4, d=3, $fn=35);
		translate([-1,5,0])cylinder(h=4, d=3, $fn=35);		
		translate([1,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-2,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-3,2.5,0])cylinder(h=4, d=5, $fn=35);
		translate([-3,-2.5,0])cylinder(h=4, d=5, $fn=35);	
		}
		}
		}
		union(){
		translate([-5,0,0])cylinder(h=4, d=3, $fn=35);
		hull(){
		translate([-4,0,4])cylinder(h=3.5, d=4.5, $fn=35);
		translate([-10,0,4])cylinder(h=3.5, d=4.5, $fn=35);
		}
		
		}
		}	
		}
}
union(){
for (a = [0:120:240]){
	hull(){
	rotate([0,0,a])translate([0,-56,10])cylinder(h=60, d=7.5, $fn=25);
	rotate([0,0,a])translate([0,-60,10])cylinder(h=60, d=10, $fn=25);
	}
	rotate([0,0,a])translate([0,-56,0])cylinder(h=60, d=5, $fn=25);
	rotate([35,0,a])cylinder(h=60, d=5, $fn=25);
	rotate([35,0,a])translate([0,0,35])cylinder(h=12, d=8, $fn=25);

}
rotate([0,0,-30])translate([11,0,51])rotate([0,10,0])cube([22,10,5], center = true);
}
}

//////////////////////////////////////////////////////////////////////
//KAMERAT
/*
difference(){
rotate([0,0,0])difference(){
union(){
for (a = [0:120:360]){
	rotate([0,0,a])
		hull(){
		translate([0,-21.5,27])cube([6.5,2,2], center = true);
		translate([21,-33.5,0])cube([2,2,2], center = true);	
		translate([-21,-33.5,0])cube([2,2,2], center = true);	
		translate([0,-38,0])cube([15,2,2], center = true);
	}

for (a = [0:120:360]){	
		rotate([0,0,a])translate([0,-40,0])rotate([0,0,90])difference(){
		union(){	
		hull(){
		translate([5,5,0])cylinder(h=4, d=3, $fn=35);
		translate([-5,5,0])cylinder(h=4, d=3, $fn=35);		
		translate([5,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-4,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-5,2.5,0])cylinder(h=4, d=5, $fn=35);
		translate([-5,-2.5,0])cylinder(h=4, d=5, $fn=35);		
		}
		}
		union(){
		translate([-5,0,0])cylinder(h=4, d=2.75, $fn=35);
		}
		}	
		}
}

translate([0,0,-1.5])difference(){
	cylinder(h=2, r=42.5, $fn=45);
	cylinder(h=2, r=37, $fn=45);	
}

hull(){
for (a = [120:120:360]){
	rotate([0,0,a])translate([0,-21.5,27])cube([7,2,2], center = true);
}
}
for (a = [120:120:360]){
	rotate([0,0,a])translate([-18,37,0])rotate([129,0,0])union(){
	
difference(){
	translate([0,0,0])cube([36,36,2]);
	translate([2,2,0])cube([32.25,32.25,2]);
}

translate([2,2,0])difference(){
	cube([5,5,2]);
	translate([2,2,0])cylinder(h=2, d=3, $fn=15);
}
translate([29,2,0])difference(){
	cube([6,5,2]);
	translate([3,2,0])cylinder(h=2, d=3 , $fn=15);
}
translate([2,29,0])difference(){
	cube([5,6,2]);
	translate([2,3,0])cylinder(h=2, d=3, $fn=15);
}
translate([30,30,0])difference(){
	cube([5,5,2]);
	translate([2,2,0])cylinder(h=2, d=3, $fn=15);
}

}
}

}
cylinder(h=45, d=13, $fn=25);
}
for (a = [0:120:240]){
	rotate([0,0,a])translate([0,-12.5,25])cylinder(h=4, d=2.5, $fn=35);
}
}
*/
/////////////////////////////////////////////////////////////////////
//KOTELO
/*
translate([0,0,5])difference(){
difference(){
union(){
union(){
translate([24.5,39.5,-27.5])cylinder(h=3, d = 6, $fn = 25);
translate([24.5,-18.5,-27.5])cylinder(h=3, d = 6, $fn = 25);
translate([-24.5,39.5,-27.5])cylinder(h=3, d = 6, $fn = 25);
translate([-24.5,-18.5,-27.5])cylinder(h=3, d = 6, $fn = 25);
}


translate([-23,5,-33.5])rotate([180,0,0])union(){
cube([8,25,10], center=true);
translate([3.5,0,5])cube([15,25,3], center=true);
}
translate([23,5,-33.5])rotate([180,0,180])union(){
cube([8,25,10], center=true);
translate([3.5,0,5])cube([15,25,3], center=true);
}

translate([0,41,-29])union(){
cube([20,2,3], center=true);
}


//hull(){
//translate([0,37,-9])cylinder(h=3, d = 4, $fn = 25);
//translate([7,38.25,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-7,38.25,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([14,36,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-14,36,-9])cylinder(h=3, d = 2, $fn = 25);
//}

//hull(){
//translate([0,-37,-9])cylinder(h=3, d = 4, $fn = 25);
//translate([7,-38.25,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-7,-38.25,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([14,-36,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-14,-36,-9])cylinder(h=3, d = 2, $fn = 25);
//}

//hull(){
//translate([-29,25.5,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-22,32,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-22,28,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-25,20,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-29,10.5,-9])cylinder(h=3, d = 2, $fn = 25);
//}

//hull(){
//translate([29,25.5,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([22,32,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([22,28,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([25,20,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([29,10.5,-9])cylinder(h=3, d = 2, $fn = 25);
//}

//hull(){
//translate([22,-32,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([22,-27,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([29,-26,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([29,-19.5,-9])cylinder(h=3, d = 2, $fn = 25);
//}

//hull(){
//translate([-22,-32,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-22,-27,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-29,-26,-9])cylinder(h=3, d = 2, $fn = 25);
//translate([-29,-19.5,-9])cylinder(h=3, d = 2, $fn = 25);
//}

translate([0,0,-18.5])union(){
translate([30.5,-28,0])cube([2.5,10,20.5], center = true);
translate([-30.5,-28,0])cube([2.5,10,20.5], center = true);

translate([30.5,28,0])cube([2.5,10,20.5], center = true);	
translate([30.5,0,0])cube([2.5,10,20.5], center = true);
	
hull(){
translate([-30.5,28,0])cube([2.5,10,20.5], center = true);
translate([-30.5,0,0])cube([2.5,10,20.5], center = true);
}
}

translate([0,0,-10])difference(){
hull(){
translate([27,39.75,-1.25])cylinder(h=3, d = 5.5, $fn = 25);
translate([27,-39.75,-1.25])cylinder(h=3, d = 5.5, $fn = 25);
translate([-27,39.75,-1.25])cylinder(h=3, d = 5.5, $fn = 25);
translate([-27,-39.75,-1.25])cylinder(h=3, d = 5.5, $fn = 25);
}
cube([42,70,3.5], center = true);
}

translate([0,0,-27.5])hull(){
translate([27,39.75,-1.25])cylinder(h=2.5, d = 5.5, $fn = 25);
translate([27,-39.75,-1.25])cylinder(h=2.5, d = 5.5, $fn = 25);
translate([-27,39.75,-1.25])cylinder(h=2.5, d = 5.5, $fn = 25);
translate([-27,-39.75,-1.25])cylinder(h=2.5, d = 5.5, $fn = 25);
}
rotate([0,0,180])translate([0,-42.5,-11.25])rotate([0,0,90])difference(){
		union(){	
		hull(){
		translate([5,5,0])cylinder(h=3, d=3, $fn=35);
		translate([-5,5,0])cylinder(h=3, d=3, $fn=35);		
		translate([5,-5,0])cylinder(h=3, d=3, $fn=35);
		translate([-4,-5,0])cylinder(h=3, d=3, $fn=35);
		translate([-5,2.5,0])cylinder(h=3, d=5, $fn=35);
		translate([-5,-2.5,0])cylinder(h=3, d=5, $fn=35);		
		}
		}
		union(){
		translate([-5,0,0])cylinder(h=3, d=2.75, $fn=35);
		}
		}	

rotate([0,0,120 + 180])translate([0,-42.5,-11.25])rotate([0,0,90])difference(){
		union(){	
		hull(){
		translate([12,5,0])cylinder(h=3, d=3, $fn=35);
		translate([-5,5,0])cylinder(h=3, d=3, $fn=35);		
		translate([11,-5,0])cylinder(h=3, d=3, $fn=35);
		translate([-4,-5,0])cylinder(h=3, d=3, $fn=35);
		translate([-5,2.5,0])cylinder(h=3, d=5, $fn=35);
		translate([-5,-2.5,0])cylinder(h=3, d=5, $fn=35);		
		}
		}
		union(){
		translate([-5,0,0])cylinder(h=3, d=2.75, $fn=35);
		}
		}
		
rotate([0,0,240 + 180])translate([0,-42.5,-11.25])rotate([0,0,90])difference(){
		union(){	
		hull(){
		translate([11,5,0])cylinder(h=3, d=3, $fn=35);
		translate([-5,5,0])cylinder(h=3, d=3, $fn=35);		
		translate([12,-5,0])cylinder(h=3, d=3, $fn=35);
		translate([-4,-5,0])cylinder(h=3, d=3, $fn=35);
		translate([-5,2.5,0])cylinder(h=3, d=5, $fn=35);
		translate([-5,-2.5,0])cylinder(h=3, d=5, $fn=35);		
		}
		}
		union(){
		translate([-5,0,0])cylinder(h=3, d=2.75, $fn=35);
		}
		}

}
cylinder(h=45, d = 13, $fn = 25);
}
union(){
translate([24.5,39.5,-29.5])cylinder(h=10, d = 3, $fn = 25);
translate([24.5,-18.5,-29.5])cylinder(h=10, d = 3, $fn = 25);
translate([-24.5,39.5,-29.5])cylinder(h=10, d = 3, $fn = 25);
translate([-24.5,-18.5,-29.5])cylinder(h=10, d = 3, $fn = 25);
	
translate([-15,-23.5,-28])cylinder(h=10, d = 4.5, $fn = 25);
translate([-15,-39.5,-28])cylinder(h=10, d = 4.5, $fn = 25);	
	
translate([-15,-23.5,-29.5])cylinder(h=10, d = 3, $fn = 25);
translate([-15,-39.5,-29.5])cylinder(h=10, d = 3, $fn = 25);
}
}
*/
/////////////////////////////////////////////////////////////////////////
//POHJA
/*
difference(){
union(){
difference(){
rotate([0,180,0])difference(){
difference(){
union(){
difference(){
difference(){
union(){
difference(){
	sphere(d=120, $fn=100);
	sphere(d=105, $fn=50);
}

for (a = [0:120:240]){
rotate([0,0,a+180])translate([0,-52.5,6.15])rotate([0,0,-90])difference(){
		union(){	
		hull(){
		union(){
		translate([4,5,0])cylinder(h=4, d=3, $fn=35);
		translate([-2,5,0])cylinder(h=4, d=3, $fn=35);		
		translate([4,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-2,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-5,2.5,0])cylinder(h=4, d=5, $fn=35);
		translate([-5,-2.5,0])cylinder(h=4, d=5, $fn=35);
		}
		translate([0,0,5])union(){
		translate([3,5,0])cylinder(h=4, d=3, $fn=35);
		translate([-2,5,0])cylinder(h=4, d=3, $fn=35);		
		translate([3,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-2,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-5,2.5,0])cylinder(h=4, d=3, $fn=35);
		translate([-5,-2.5,0])cylinder(h=4, d=3, $fn=35);	
		}
		translate([0,0,10])union(){
		translate([1,5,0])cylinder(h=4, d=3, $fn=35);
		translate([-1,5,0])cylinder(h=4, d=3, $fn=35);		
		translate([1,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-2,-5,0])cylinder(h=4, d=3, $fn=35);
		translate([-3,2.5,0])cylinder(h=4, d=3, $fn=35);
		translate([-3,-2.5,0])cylinder(h=4, d=3, $fn=35);	
		}
		}
		}
		union(){
		translate([-5,0,0])cylinder(h=4, d=3, $fn=35);
		translate([-5,0,0])cube([8.5,15,1.5], center=true);
		hull(){
		translate([-4,0,4])cylinder(h=4.5, d=3.5, $fn=35);
		translate([-10,0,4])cylinder(h=4.5, d=3.5, $fn=35);
		}
		
		}
		}	
}
}
	union(){
	translate([0,0,-60])cube([120,120,120], center = true);
}
}
union(){
for (a = [0:120:240]){
	hull(){
	rotate([0,0,a])translate([0,-56,10])cylinder(h=3.5, d=7.5, $fn=25);
	rotate([0,0,a])translate([0,-60,10])cylinder(h=3.5, d=10, $fn=25);
	}
	rotate([0,0,a])translate([0,-56,0])cylinder(h=13.5, d=5, $fn=25);
}
}
}
rotate([0,0,-90])translate([0,36,28])rotate([-50,0,0])difference(){
		difference(){
		cylinder(h=12.5, d=25, $fn=25);
		cylinder(h=12.5, d=21.5, $fn=50);
		}
		cube([25,10,20], center = true);
		
}

}
rotate([0,0,-90])translate([0,36,28])rotate([-50,0,0])union(){
for (a = [0:60:360]){
	cylinder(h=15, d=3, $fn=25);
	rotate([0,0,a])translate([0,4,0])cylinder(h=15, d=3, $fn=25);
	rotate([0,0,a])translate([3.5,6,0])cylinder(h=15, d=3, $fn=25);
	rotate([0,0,a])translate([0,9,0])cylinder(h=15, d=3, $fn=25);
}
}
}

rotate([0,0,120])translate([-11,45,34])rotate([-50,0,0])linear_extrude(height = 5){
	text("Savox", font="tohoma:style=bold", size=4.5, spacing=1.1);
	translate([-7,-7,0])text("ThrowCam", font="tohoma:style=bold" ,size=4.5 , spacing=1.1);
}
}
cube([61,86,47.75], center=true);
}
hull(){
translate([0,0,-53.5])cylinder(h=5, d=45, $fn=35);	
translate([0,0,-55])cylinder(h=5, d=25, $fn=35);
}
}
union(){
translate([0,0,-67.5])cube([75,75,25], center=true);

for (a = [0:120:240]){
	rotate([35,180,a])cylinder(h=60, d=5, $fn=25);

}

translate([0,0,-52])union(){
translate([0,-10,0])union(){
translate([-3,5.25,0])cylinder(h=5, d=2.25, $fn=25);
translate([-3,-5.25,0])cylinder(h=5, d=2.25, $fn=25);
}
translate([-5,10,0])union(){
translate([-3,5,0])cylinder(h=5, d=2.25, $fn=25);
translate([-3,-5,0])cylinder(h=5, d=2.25, $fn=25);
}	
}
}
}
*/
//////////////////////////////////////////////////////////////////////////
//PEHMUSTE
/*
difference(){
union(){
for (b = [0:120:240]){
		rotate([0,0,b])color("Gray")union(){
        difference(){
        hull(){
            rotate([-20,0,-25])cylinder(h=75, d=15, $fn=35);
            rotate([-20,0,25])cylinder(h=75, d=15, $fn=35);
            rotate([-56.5,0,-45])cylinder(h=75, d=15, $fn=35);
            rotate([-56.5,0,45])cylinder(h=75, d=15, $fn=35);
            rotate([-80,0,0])cylinder(h=75, d=15, $fn=35);
            rotate([-80,0,-45])cylinder(h=75, d=15, $fn=35);
            rotate([-80,0,45])cylinder(h=75, d=15, $fn=35);
        }
            hull(){
            rotate([-32.5,0,0])translate([0,0,55])cylinder(h=15, d=5, $fn=35);
            rotate([-32.5,0,0])translate([0,0,75])cylinder(h=15, d=30, $fn=35);   
            rotate([-57,0,0])translate([0,0,55])cylinder(h=15, d=25, $fn=35);
            rotate([-57,0,0])translate([0,0,75])cylinder(h=15, d=60, $fn=35);  
            }
        }
    }
    }

rotate([0,180,0])union(){
for (b = [0:120:240]){
		union(){
        difference(){
        rotate([0,0,b])color("Gray")hull(){
            rotate([-20,0,-30])cylinder(h=75, d=15, $fn=35);
            rotate([-20,0,30])cylinder(h=75, d=15, $fn=35);
            rotate([-56.5,0,-45])cylinder(h=75, d=15, $fn=35);
            rotate([-56.5,0,45])cylinder(h=75, d=15, $fn=35);
            rotate([-80,0,0])cylinder(h=75, d=15, $fn=35);
            rotate([-80,0,-45])cylinder(h=75, d=15, $fn=35);
            rotate([-80,0,45])cylinder(h=75, d=15, $fn=35);
        }
        translate([0,0,85])sphere(d=75, $fn=35);
        rotate([-51.5,0,-90])hull(){
        translate([0,0,55])cylinder(h=15, d=18, $fn=35);
        translate([0,0,75])cylinder(h=15, d=40, $fn=35);  
        }
        }
    }
    }
}
}
union(){
color("Gray")sphere(d=120, $fn=35);
difference(){
color("Gray")sphere(d=160, $fn=35);    
color("Gray")sphere(d=135, $fn=100);
}
}
}
*/