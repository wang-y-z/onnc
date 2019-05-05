import numpy as np

def tensor():
    # dims: [1, 1, 28, 28]
    input_0 = np.array(
        [
            [
                [
                    [
                        0.0, 	# 0,0,0,0
                        0.0, 	# 0,0,0,1
                        0.0, 	# 0,0,0,2
                        0.0, 	# 0,0,0,3
                        0.0, 	# 0,0,0,4
                        0.0, 	# 0,0,0,5
                        0.0, 	# 0,0,0,6
                        0.0, 	# 0,0,0,7
                        0.0, 	# 0,0,0,8
                        1.0, 	# 0,0,0,9
                        3.0, 	# 0,0,0,10
                        0.0, 	# 0,0,0,11
                        0.0, 	# 0,0,0,12
                        4.0, 	# 0,0,0,13
                        2.0, 	# 0,0,0,14
                        0.0, 	# 0,0,0,15
                        11.0, 	# 0,0,0,16
                        0.0, 	# 0,0,0,17
                        0.0, 	# 0,0,0,18
                        14.0, 	# 0,0,0,19
                        1.0, 	# 0,0,0,20
                        0.0, 	# 0,0,0,21
                        19.0, 	# 0,0,0,22
                        0.0, 	# 0,0,0,23
                        0.0, 	# 0,0,0,24
                        0.0, 	# 0,0,0,25
                        0.0, 	# 0,0,0,26
                        0.0, 	# 0,0,0,27
                    ],
                    [
                        0.0, 	# 0,0,1,0
                        0.0, 	# 0,0,1,1
                        0.0, 	# 0,0,1,2
                        0.0, 	# 0,0,1,3
                        0.0, 	# 0,0,1,4
                        0.0, 	# 0,0,1,5
                        0.0, 	# 0,0,1,6
                        0.0, 	# 0,0,1,7
                        0.0, 	# 0,0,1,8
                        12.0, 	# 0,0,1,9
                        0.0, 	# 0,0,1,10
                        0.0, 	# 0,0,1,11
                        7.0, 	# 0,0,1,12
                        0.0, 	# 0,0,1,13
                        1.0, 	# 0,0,1,14
                        10.0, 	# 0,0,1,15
                        0.0, 	# 0,0,1,16
                        2.0, 	# 0,0,1,17
                        2.0, 	# 0,0,1,18
                        16.0, 	# 0,0,1,19
                        0.0, 	# 0,0,1,20
                        3.0, 	# 0,0,1,21
                        3.0, 	# 0,0,1,22
                        0.0, 	# 0,0,1,23
                        0.0, 	# 0,0,1,24
                        0.0, 	# 0,0,1,25
                        0.0, 	# 0,0,1,26
                        0.0, 	# 0,0,1,27
                    ],
                    [
                        0.0, 	# 0,0,2,0
                        0.0, 	# 0,0,2,1
                        0.0, 	# 0,0,2,2
                        0.0, 	# 0,0,2,3
                        0.0, 	# 0,0,2,4
                        0.0, 	# 0,0,2,5
                        0.0, 	# 0,0,2,6
                        0.0, 	# 0,0,2,7
                        7.0, 	# 0,0,2,8
                        8.0, 	# 0,0,2,9
                        0.0, 	# 0,0,2,10
                        8.0, 	# 0,0,2,11
                        0.0, 	# 0,0,2,12
                        0.0, 	# 0,0,2,13
                        8.0, 	# 0,0,2,14
                        0.0, 	# 0,0,2,15
                        0.0, 	# 0,0,2,16
                        19.0, 	# 0,0,2,17
                        0.0, 	# 0,0,2,18
                        0.0, 	# 0,0,2,19
                        1.0, 	# 0,0,2,20
                        21.0, 	# 0,0,2,21
                        0.0, 	# 0,0,2,22
                        4.0, 	# 0,0,2,23
                        0.0, 	# 0,0,2,24
                        0.0, 	# 0,0,2,25
                        0.0, 	# 0,0,2,26
                        0.0, 	# 0,0,2,27
                    ],
                    [
                        0.0, 	# 0,0,3,0
                        0.0, 	# 0,0,3,1
                        0.0, 	# 0,0,3,2
                        0.0, 	# 0,0,3,3
                        0.0, 	# 0,0,3,4
                        0.0, 	# 0,0,3,5
                        0.0, 	# 0,0,3,6
                        0.0, 	# 0,0,3,7
                        0.0, 	# 0,0,3,8
                        0.0, 	# 0,0,3,9
                        1.0, 	# 0,0,3,10
                        0.0, 	# 0,0,3,11
                        0.0, 	# 0,0,3,12
                        1.0, 	# 0,0,3,13
                        0.0, 	# 0,0,3,14
                        0.0, 	# 0,0,3,15
                        0.0, 	# 0,0,3,16
                        0.0, 	# 0,0,3,17
                        0.0, 	# 0,0,3,18
                        11.0, 	# 0,0,3,19
                        0.0, 	# 0,0,3,20
                        0.0, 	# 0,0,3,21
                        10.0, 	# 0,0,3,22
                        3.0, 	# 0,0,3,23
                        0.0, 	# 0,0,3,24
                        0.0, 	# 0,0,3,25
                        0.0, 	# 0,0,3,26
                        0.0, 	# 0,0,3,27
                    ],
                    [
                        0.0, 	# 0,0,4,0
                        0.0, 	# 0,0,4,1
                        0.0, 	# 0,0,4,2
                        0.0, 	# 0,0,4,3
                        0.0, 	# 0,0,4,4
                        0.0, 	# 0,0,4,5
                        0.0, 	# 0,0,4,6
                        0.0, 	# 0,0,4,7
                        13.0, 	# 0,0,4,8
                        0.0, 	# 0,0,4,9
                        15.0, 	# 0,0,4,10
                        10.0, 	# 0,0,4,11
                        26.0, 	# 0,0,4,12
                        34.0, 	# 0,0,4,13
                        17.0, 	# 0,0,4,14
                        77.0, 	# 0,0,4,15
                        181.0, 	# 0,0,4,16
                        178.0, 	# 0,0,4,17
                        35.0, 	# 0,0,4,18
                        4.0, 	# 0,0,4,19
                        0.0, 	# 0,0,4,20
                        0.0, 	# 0,0,4,21
                        0.0, 	# 0,0,4,22
                        0.0, 	# 0,0,4,23
                        0.0, 	# 0,0,4,24
                        0.0, 	# 0,0,4,25
                        0.0, 	# 0,0,4,26
                        0.0, 	# 0,0,4,27
                    ],
                    [
                        0.0, 	# 0,0,5,0
                        0.0, 	# 0,0,5,1
                        0.0, 	# 0,0,5,2
                        0.0, 	# 0,0,5,3
                        0.0, 	# 0,0,5,4
                        0.0, 	# 0,0,5,5
                        0.0, 	# 0,0,5,6
                        0.0, 	# 0,0,5,7
                        0.0, 	# 0,0,5,8
                        0.0, 	# 0,0,5,9
                        150.0, 	# 0,0,5,10
                        254.0, 	# 0,0,5,11
                        250.0, 	# 0,0,5,12
                        251.0, 	# 0,0,5,13
                        243.0, 	# 0,0,5,14
                        252.0, 	# 0,0,5,15
                        252.0, 	# 0,0,5,16
                        255.0, 	# 0,0,5,17
                        45.0, 	# 0,0,5,18
                        6.0, 	# 0,0,5,19
                        0.0, 	# 0,0,5,20
                        5.0, 	# 0,0,5,21
                        0.0, 	# 0,0,5,22
                        9.0, 	# 0,0,5,23
                        0.0, 	# 0,0,5,24
                        0.0, 	# 0,0,5,25
                        0.0, 	# 0,0,5,26
                        0.0, 	# 0,0,5,27
                    ],
                    [
                        0.0, 	# 0,0,6,0
                        0.0, 	# 0,0,6,1
                        0.0, 	# 0,0,6,2
                        0.0, 	# 0,0,6,3
                        0.0, 	# 0,0,6,4
                        0.0, 	# 0,0,6,5
                        0.0, 	# 0,0,6,6
                        0.0, 	# 0,0,6,7
                        7.0, 	# 0,0,6,8
                        72.0, 	# 0,0,6,9
                        205.0, 	# 0,0,6,10
                        255.0, 	# 0,0,6,11
                        238.0, 	# 0,0,6,12
                        243.0, 	# 0,0,6,13
                        255.0, 	# 0,0,6,14
                        254.0, 	# 0,0,6,15
                        251.0, 	# 0,0,6,16
                        248.0, 	# 0,0,6,17
                        201.0, 	# 0,0,6,18
                        198.0, 	# 0,0,6,19
                        57.0, 	# 0,0,6,20
                        0.0, 	# 0,0,6,21
                        19.0, 	# 0,0,6,22
                        0.0, 	# 0,0,6,23
                        0.0, 	# 0,0,6,24
                        0.0, 	# 0,0,6,25
                        0.0, 	# 0,0,6,26
                        0.0, 	# 0,0,6,27
                    ],
                    [
                        0.0, 	# 0,0,7,0
                        0.0, 	# 0,0,7,1
                        0.0, 	# 0,0,7,2
                        0.0, 	# 0,0,7,3
                        0.0, 	# 0,0,7,4
                        0.0, 	# 0,0,7,5
                        0.0, 	# 0,0,7,6
                        0.0, 	# 0,0,7,7
                        0.0, 	# 0,0,7,8
                        218.0, 	# 0,0,7,9
                        255.0, 	# 0,0,7,10
                        241.0, 	# 0,0,7,11
                        255.0, 	# 0,0,7,12
                        249.0, 	# 0,0,7,13
                        250.0, 	# 0,0,7,14
                        251.0, 	# 0,0,7,15
                        250.0, 	# 0,0,7,16
                        255.0, 	# 0,0,7,17
                        255.0, 	# 0,0,7,18
                        242.0, 	# 0,0,7,19
                        224.0, 	# 0,0,7,20
                        49.0, 	# 0,0,7,21
                        0.0, 	# 0,0,7,22
                        12.0, 	# 0,0,7,23
                        0.0, 	# 0,0,7,24
                        0.0, 	# 0,0,7,25
                        0.0, 	# 0,0,7,26
                        0.0, 	# 0,0,7,27
                    ],
                    [
                        0.0, 	# 0,0,8,0
                        0.0, 	# 0,0,8,1
                        1.0, 	# 0,0,8,2
                        2.0, 	# 0,0,8,3
                        3.0, 	# 0,0,8,4
                        2.0, 	# 0,0,8,5
                        2.0, 	# 0,0,8,6
                        1.0, 	# 0,0,8,7
                        0.0, 	# 0,0,8,8
                        65.0, 	# 0,0,8,9
                        228.0, 	# 0,0,8,10
                        255.0, 	# 0,0,8,11
                        254.0, 	# 0,0,8,12
                        244.0, 	# 0,0,8,13
                        119.0, 	# 0,0,8,14
                        34.0, 	# 0,0,8,15
                        41.0, 	# 0,0,8,16
                        110.0, 	# 0,0,8,17
                        250.0, 	# 0,0,8,18
                        255.0, 	# 0,0,8,19
                        248.0, 	# 0,0,8,20
                        124.0, 	# 0,0,8,21
                        20.0, 	# 0,0,8,22
                        0.0, 	# 0,0,8,23
                        0.0, 	# 0,0,8,24
                        0.0, 	# 0,0,8,25
                        0.0, 	# 0,0,8,26
                        0.0, 	# 0,0,8,27
                    ],
                    [
                        1.0, 	# 0,0,9,0
                        1.0, 	# 0,0,9,1
                        0.0, 	# 0,0,9,2
                        0.0, 	# 0,0,9,3
                        0.0, 	# 0,0,9,4
                        0.0, 	# 0,0,9,5
                        0.0, 	# 0,0,9,6
                        0.0, 	# 0,0,9,7
                        12.0, 	# 0,0,9,8
                        0.0, 	# 0,0,9,9
                        62.0, 	# 0,0,9,10
                        103.0, 	# 0,0,9,11
                        113.0, 	# 0,0,9,12
                        117.0, 	# 0,0,9,13
                        34.0, 	# 0,0,9,14
                        0.0, 	# 0,0,9,15
                        0.0, 	# 0,0,9,16
                        0.0, 	# 0,0,9,17
                        200.0, 	# 0,0,9,18
                        244.0, 	# 0,0,9,19
                        255.0, 	# 0,0,9,20
                        255.0, 	# 0,0,9,21
                        0.0, 	# 0,0,9,22
                        12.0, 	# 0,0,9,23
                        0.0, 	# 0,0,9,24
                        0.0, 	# 0,0,9,25
                        0.0, 	# 0,0,9,26
                        0.0, 	# 0,0,9,27
                    ],
                    [
                        2.0, 	# 0,0,10,0
                        1.0, 	# 0,0,10,1
                        0.0, 	# 0,0,10,2
                        0.0, 	# 0,0,10,3
                        0.0, 	# 0,0,10,4
                        0.0, 	# 0,0,10,5
                        1.0, 	# 0,0,10,6
                        2.0, 	# 0,0,10,7
                        0.0, 	# 0,0,10,8
                        0.0, 	# 0,0,10,9
                        2.0, 	# 0,0,10,10
                        4.0, 	# 0,0,10,11
                        0.0, 	# 0,0,10,12
                        11.0, 	# 0,0,10,13
                        0.0, 	# 0,0,10,14
                        7.0, 	# 0,0,10,15
                        6.0, 	# 0,0,10,16
                        0.0, 	# 0,0,10,17
                        75.0, 	# 0,0,10,18
                        244.0, 	# 0,0,10,19
                        255.0, 	# 0,0,10,20
                        255.0, 	# 0,0,10,21
                        4.0, 	# 0,0,10,22
                        0.0, 	# 0,0,10,23
                        0.0, 	# 0,0,10,24
                        0.0, 	# 0,0,10,25
                        0.0, 	# 0,0,10,26
                        0.0, 	# 0,0,10,27
                    ],
                    [
                        0.0, 	# 0,0,11,0
                        0.0, 	# 0,0,11,1
                        0.0, 	# 0,0,11,2
                        1.0, 	# 0,0,11,3
                        2.0, 	# 0,0,11,4
                        3.0, 	# 0,0,11,5
                        4.0, 	# 0,0,11,6
                        4.0, 	# 0,0,11,7
                        0.0, 	# 0,0,11,8
                        14.0, 	# 0,0,11,9
                        0.0, 	# 0,0,11,10
                        0.0, 	# 0,0,11,11
                        0.0, 	# 0,0,11,12
                        9.0, 	# 0,0,11,13
                        0.0, 	# 0,0,11,14
                        2.0, 	# 0,0,11,15
                        0.0, 	# 0,0,11,16
                        0.0, 	# 0,0,11,17
                        34.0, 	# 0,0,11,18
                        255.0, 	# 0,0,11,19
                        255.0, 	# 0,0,11,20
                        253.0, 	# 0,0,11,21
                        10.0, 	# 0,0,11,22
                        10.0, 	# 0,0,11,23
                        0.0, 	# 0,0,11,24
                        0.0, 	# 0,0,11,25
                        0.0, 	# 0,0,11,26
                        0.0, 	# 0,0,11,27
                    ],
                    [
                        0.0, 	# 0,0,12,0
                        0.0, 	# 0,0,12,1
                        1.0, 	# 0,0,12,2
                        2.0, 	# 0,0,12,3
                        3.0, 	# 0,0,12,4
                        2.0, 	# 0,0,12,5
                        0.0, 	# 0,0,12,6
                        0.0, 	# 0,0,12,7
                        3.0, 	# 0,0,12,8
                        2.0, 	# 0,0,12,9
                        0.0, 	# 0,0,12,10
                        13.0, 	# 0,0,12,11
                        11.0, 	# 0,0,12,12
                        0.0, 	# 0,0,12,13
                        0.0, 	# 0,0,12,14
                        0.0, 	# 0,0,12,15
                        6.0, 	# 0,0,12,16
                        12.0, 	# 0,0,12,17
                        99.0, 	# 0,0,12,18
                        255.0, 	# 0,0,12,19
                        254.0, 	# 0,0,12,20
                        248.0, 	# 0,0,12,21
                        15.0, 	# 0,0,12,22
                        12.0, 	# 0,0,12,23
                        0.0, 	# 0,0,12,24
                        0.0, 	# 0,0,12,25
                        0.0, 	# 0,0,12,26
                        0.0, 	# 0,0,12,27
                    ],
                    [
                        0.0, 	# 0,0,13,0
                        1.0, 	# 0,0,13,1
                        1.0, 	# 0,0,13,2
                        1.0, 	# 0,0,13,3
                        0.0, 	# 0,0,13,4
                        0.0, 	# 0,0,13,5
                        0.0, 	# 0,0,13,6
                        0.0, 	# 0,0,13,7
                        1.0, 	# 0,0,13,8
                        1.0, 	# 0,0,13,9
                        0.0, 	# 0,0,13,10
                        0.0, 	# 0,0,13,11
                        5.0, 	# 0,0,13,12
                        6.0, 	# 0,0,13,13
                        11.0, 	# 0,0,13,14
                        0.0, 	# 0,0,13,15
                        0.0, 	# 0,0,13,16
                        17.0, 	# 0,0,13,17
                        184.0, 	# 0,0,13,18
                        247.0, 	# 0,0,13,19
                        255.0, 	# 0,0,13,20
                        243.0, 	# 0,0,13,21
                        13.0, 	# 0,0,13,22
                        0.0, 	# 0,0,13,23
                        0.0, 	# 0,0,13,24
                        0.0, 	# 0,0,13,25
                        0.0, 	# 0,0,13,26
                        0.0, 	# 0,0,13,27
                    ],
                    [
                        3.0, 	# 0,0,14,0
                        2.0, 	# 0,0,14,1
                        0.0, 	# 0,0,14,2
                        0.0, 	# 0,0,14,3
                        0.0, 	# 0,0,14,4
                        0.0, 	# 0,0,14,5
                        2.0, 	# 0,0,14,6
                        4.0, 	# 0,0,14,7
                        4.0, 	# 0,0,14,8
                        0.0, 	# 0,0,14,9
                        11.0, 	# 0,0,14,10
                        0.0, 	# 0,0,14,11
                        51.0, 	# 0,0,14,12
                        94.0, 	# 0,0,14,13
                        85.0, 	# 0,0,14,14
                        5.0, 	# 0,0,14,15
                        5.0, 	# 0,0,14,16
                        25.0, 	# 0,0,14,17
                        246.0, 	# 0,0,14,18
                        246.0, 	# 0,0,14,19
                        255.0, 	# 0,0,14,20
                        208.0, 	# 0,0,14,21
                        0.0, 	# 0,0,14,22
                        9.0, 	# 0,0,14,23
                        0.0, 	# 0,0,14,24
                        0.0, 	# 0,0,14,25
                        0.0, 	# 0,0,14,26
                        0.0, 	# 0,0,14,27
                    ],
                    [
                        4.0, 	# 0,0,15,0
                        1.0, 	# 0,0,15,1
                        0.0, 	# 0,0,15,2
                        0.0, 	# 0,0,15,3
                        1.0, 	# 0,0,15,4
                        7.0, 	# 0,0,15,5
                        15.0, 	# 0,0,15,6
                        19.0, 	# 0,0,15,7
                        99.0, 	# 0,0,15,8
                        103.0, 	# 0,0,15,9
                        182.0, 	# 0,0,15,10
                        189.0, 	# 0,0,15,11
                        237.0, 	# 0,0,15,12
                        253.0, 	# 0,0,15,13
                        252.0, 	# 0,0,15,14
                        191.0, 	# 0,0,15,15
                        190.0, 	# 0,0,15,16
                        227.0, 	# 0,0,15,17
                        243.0, 	# 0,0,15,18
                        252.0, 	# 0,0,15,19
                        210.0, 	# 0,0,15,20
                        18.0, 	# 0,0,15,21
                        7.0, 	# 0,0,15,22
                        0.0, 	# 0,0,15,23
                        0.0, 	# 0,0,15,24
                        0.0, 	# 0,0,15,25
                        0.0, 	# 0,0,15,26
                        0.0, 	# 0,0,15,27
                    ],
                    [
                        0.0, 	# 0,0,16,0
                        4.0, 	# 0,0,16,1
                        0.0, 	# 0,0,16,2
                        0.0, 	# 0,0,16,3
                        32.0, 	# 0,0,16,4
                        109.0, 	# 0,0,16,5
                        185.0, 	# 0,0,16,6
                        247.0, 	# 0,0,16,7
                        255.0, 	# 0,0,16,8
                        242.0, 	# 0,0,16,9
                        255.0, 	# 0,0,16,10
                        244.0, 	# 0,0,16,11
                        255.0, 	# 0,0,16,12
                        255.0, 	# 0,0,16,13
                        242.0, 	# 0,0,16,14
                        251.0, 	# 0,0,16,15
                        255.0, 	# 0,0,16,16
                        240.0, 	# 0,0,16,17
                        255.0, 	# 0,0,16,18
                        255.0, 	# 0,0,16,19
                        218.0, 	# 0,0,16,20
                        124.0, 	# 0,0,16,21
                        9.0, 	# 0,0,16,22
                        0.0, 	# 0,0,16,23
                        0.0, 	# 0,0,16,24
                        0.0, 	# 0,0,16,25
                        0.0, 	# 0,0,16,26
                        0.0, 	# 0,0,16,27
                    ],
                    [
                        2.0, 	# 0,0,17,0
                        0.0, 	# 0,0,17,1
                        0.0, 	# 0,0,17,2
                        0.0, 	# 0,0,17,3
                        127.0, 	# 0,0,17,4
                        255.0, 	# 0,0,17,5
                        235.0, 	# 0,0,17,6
                        255.0, 	# 0,0,17,7
                        255.0, 	# 0,0,17,8
                        247.0, 	# 0,0,17,9
                        229.0, 	# 0,0,17,10
                        212.0, 	# 0,0,17,11
                        242.0, 	# 0,0,17,12
                        250.0, 	# 0,0,17,13
                        255.0, 	# 0,0,17,14
                        255.0, 	# 0,0,17,15
                        248.0, 	# 0,0,17,16
                        255.0, 	# 0,0,17,17
                        253.0, 	# 0,0,17,18
                        249.0, 	# 0,0,17,19
                        255.0, 	# 0,0,17,20
                        243.0, 	# 0,0,17,21
                        170.0, 	# 0,0,17,22
                        12.0, 	# 0,0,17,23
                        0.0, 	# 0,0,17,24
                        0.0, 	# 0,0,17,25
                        0.0, 	# 0,0,17,26
                        0.0, 	# 0,0,17,27
                    ],
                    [
                        0.0, 	# 0,0,18,0
                        11.0, 	# 0,0,18,1
                        0.0, 	# 0,0,18,2
                        9.0, 	# 0,0,18,3
                        253.0, 	# 0,0,18,4
                        255.0, 	# 0,0,18,5
                        255.0, 	# 0,0,18,6
                        233.0, 	# 0,0,18,7
                        202.0, 	# 0,0,18,8
                        85.0, 	# 0,0,18,9
                        0.0, 	# 0,0,18,10
                        53.0, 	# 0,0,18,11
                        196.0, 	# 0,0,18,12
                        238.0, 	# 0,0,18,13
                        255.0, 	# 0,0,18,14
                        227.0, 	# 0,0,18,15
                        238.0, 	# 0,0,18,16
                        142.0, 	# 0,0,18,17
                        109.0, 	# 0,0,18,18
                        193.0, 	# 0,0,18,19
                        255.0, 	# 0,0,18,20
                        240.0, 	# 0,0,18,21
                        255.0, 	# 0,0,18,22
                        180.0, 	# 0,0,18,23
                        0.0, 	# 0,0,18,24
                        0.0, 	# 0,0,18,25
                        0.0, 	# 0,0,18,26
                        0.0, 	# 0,0,18,27
                    ],
                    [
                        6.0, 	# 0,0,19,0
                        0.0, 	# 0,0,19,1
                        22.0, 	# 0,0,19,2
                        1.0, 	# 0,0,19,3
                        245.0, 	# 0,0,19,4
                        243.0, 	# 0,0,19,5
                        254.0, 	# 0,0,19,6
                        255.0, 	# 0,0,19,7
                        217.0, 	# 0,0,19,8
                        235.0, 	# 0,0,19,9
                        226.0, 	# 0,0,19,10
                        213.0, 	# 0,0,19,11
                        244.0, 	# 0,0,19,12
                        251.0, 	# 0,0,19,13
                        255.0, 	# 0,0,19,14
                        239.0, 	# 0,0,19,15
                        77.0, 	# 0,0,19,16
                        0.0, 	# 0,0,19,17
                        0.0, 	# 0,0,19,18
                        20.0, 	# 0,0,19,19
                        182.0, 	# 0,0,19,20
                        247.0, 	# 0,0,19,21
                        239.0, 	# 0,0,19,22
                        243.0, 	# 0,0,19,23
                        0.0, 	# 0,0,19,24
                        0.0, 	# 0,0,19,25
                        0.0, 	# 0,0,19,26
                        0.0, 	# 0,0,19,27
                    ],
                    [
                        0.0, 	# 0,0,20,0
                        0.0, 	# 0,0,20,1
                        0.0, 	# 0,0,20,2
                        4.0, 	# 0,0,20,3
                        165.0, 	# 0,0,20,4
                        251.0, 	# 0,0,20,5
                        255.0, 	# 0,0,20,6
                        245.0, 	# 0,0,20,7
                        255.0, 	# 0,0,20,8
                        242.0, 	# 0,0,20,9
                        253.0, 	# 0,0,20,10
                        250.0, 	# 0,0,20,11
                        255.0, 	# 0,0,20,12
                        197.0, 	# 0,0,20,13
                        107.0, 	# 0,0,20,14
                        59.0, 	# 0,0,20,15
                        0.0, 	# 0,0,20,16
                        18.0, 	# 0,0,20,17
                        2.0, 	# 0,0,20,18
                        6.0, 	# 0,0,20,19
                        0.0, 	# 0,0,20,20
                        54.0, 	# 0,0,20,21
                        255.0, 	# 0,0,20,22
                        158.0, 	# 0,0,20,23
                        0.0, 	# 0,0,20,24
                        0.0, 	# 0,0,20,25
                        0.0, 	# 0,0,20,26
                        0.0, 	# 0,0,20,27
                    ],
                    [
                        0.0, 	# 0,0,21,0
                        24.0, 	# 0,0,21,1
                        0.0, 	# 0,0,21,2
                        0.0, 	# 0,0,21,3
                        6.0, 	# 0,0,21,4
                        34.0, 	# 0,0,21,5
                        167.0, 	# 0,0,21,6
                        194.0, 	# 0,0,21,7
                        176.0, 	# 0,0,21,8
                        183.0, 	# 0,0,21,9
                        164.0, 	# 0,0,21,10
                        44.0, 	# 0,0,21,11
                        2.0, 	# 0,0,21,12
                        10.0, 	# 0,0,21,13
                        6.0, 	# 0,0,21,14
                        6.0, 	# 0,0,21,15
                        0.0, 	# 0,0,21,16
                        0.0, 	# 0,0,21,17
                        5.0, 	# 0,0,21,18
                        0.0, 	# 0,0,21,19
                        1.0, 	# 0,0,21,20
                        0.0, 	# 0,0,21,21
                        14.0, 	# 0,0,21,22
                        2.0, 	# 0,0,21,23
                        0.0, 	# 0,0,21,24
                        0.0, 	# 0,0,21,25
                        0.0, 	# 0,0,21,26
                        0.0, 	# 0,0,21,27
                    ],
                    [
                        10.0, 	# 0,0,22,0
                        0.0, 	# 0,0,22,1
                        14.0, 	# 0,0,22,2
                        0.0, 	# 0,0,22,3
                        12.0, 	# 0,0,22,4
                        0.0, 	# 0,0,22,5
                        5.0, 	# 0,0,22,6
                        0.0, 	# 0,0,22,7
                        1.0, 	# 0,0,22,8
                        0.0, 	# 0,0,22,9
                        6.0, 	# 0,0,22,10
                        0.0, 	# 0,0,22,11
                        7.0, 	# 0,0,22,12
                        0.0, 	# 0,0,22,13
                        0.0, 	# 0,0,22,14
                        0.0, 	# 0,0,22,15
                        8.0, 	# 0,0,22,16
                        0.0, 	# 0,0,22,17
                        10.0, 	# 0,0,22,18
                        0.0, 	# 0,0,22,19
                        5.0, 	# 0,0,22,20
                        0.0, 	# 0,0,22,21
                        0.0, 	# 0,0,22,22
                        10.0, 	# 0,0,22,23
                        0.0, 	# 0,0,22,24
                        0.0, 	# 0,0,22,25
                        0.0, 	# 0,0,22,26
                        0.0, 	# 0,0,22,27
                    ],
                    [
                        0.0, 	# 0,0,23,0
                        14.0, 	# 0,0,23,1
                        0.0, 	# 0,0,23,2
                        4.0, 	# 0,0,23,3
                        0.0, 	# 0,0,23,4
                        0.0, 	# 0,0,23,5
                        25.0, 	# 0,0,23,6
                        0.0, 	# 0,0,23,7
                        0.0, 	# 0,0,23,8
                        9.0, 	# 0,0,23,9
                        0.0, 	# 0,0,23,10
                        0.0, 	# 0,0,23,11
                        9.0, 	# 0,0,23,12
                        0.0, 	# 0,0,23,13
                        11.0, 	# 0,0,23,14
                        0.0, 	# 0,0,23,15
                        1.0, 	# 0,0,23,16
                        0.0, 	# 0,0,23,17
                        0.0, 	# 0,0,23,18
                        2.0, 	# 0,0,23,19
                        0.0, 	# 0,0,23,20
                        0.0, 	# 0,0,23,21
                        7.0, 	# 0,0,23,22
                        0.0, 	# 0,0,23,23
                        0.0, 	# 0,0,23,24
                        0.0, 	# 0,0,23,25
                        0.0, 	# 0,0,23,26
                        0.0, 	# 0,0,23,27
                    ],
                    [
                        0.0, 	# 0,0,24,0
                        0.0, 	# 0,0,24,1
                        0.0, 	# 0,0,24,2
                        0.0, 	# 0,0,24,3
                        0.0, 	# 0,0,24,4
                        0.0, 	# 0,0,24,5
                        0.0, 	# 0,0,24,6
                        0.0, 	# 0,0,24,7
                        0.0, 	# 0,0,24,8
                        0.0, 	# 0,0,24,9
                        0.0, 	# 0,0,24,10
                        0.0, 	# 0,0,24,11
                        0.0, 	# 0,0,24,12
                        0.0, 	# 0,0,24,13
                        0.0, 	# 0,0,24,14
                        0.0, 	# 0,0,24,15
                        0.0, 	# 0,0,24,16
                        0.0, 	# 0,0,24,17
                        0.0, 	# 0,0,24,18
                        0.0, 	# 0,0,24,19
                        0.0, 	# 0,0,24,20
                        0.0, 	# 0,0,24,21
                        0.0, 	# 0,0,24,22
                        0.0, 	# 0,0,24,23
                        0.0, 	# 0,0,24,24
                        0.0, 	# 0,0,24,25
                        0.0, 	# 0,0,24,26
                        0.0, 	# 0,0,24,27
                    ],
                    [
                        0.0, 	# 0,0,25,0
                        0.0, 	# 0,0,25,1
                        0.0, 	# 0,0,25,2
                        0.0, 	# 0,0,25,3
                        0.0, 	# 0,0,25,4
                        0.0, 	# 0,0,25,5
                        0.0, 	# 0,0,25,6
                        0.0, 	# 0,0,25,7
                        0.0, 	# 0,0,25,8
                        0.0, 	# 0,0,25,9
                        0.0, 	# 0,0,25,10
                        0.0, 	# 0,0,25,11
                        0.0, 	# 0,0,25,12
                        0.0, 	# 0,0,25,13
                        0.0, 	# 0,0,25,14
                        0.0, 	# 0,0,25,15
                        0.0, 	# 0,0,25,16
                        0.0, 	# 0,0,25,17
                        0.0, 	# 0,0,25,18
                        0.0, 	# 0,0,25,19
                        0.0, 	# 0,0,25,20
                        0.0, 	# 0,0,25,21
                        0.0, 	# 0,0,25,22
                        0.0, 	# 0,0,25,23
                        0.0, 	# 0,0,25,24
                        0.0, 	# 0,0,25,25
                        0.0, 	# 0,0,25,26
                        0.0, 	# 0,0,25,27
                    ],
                    [
                        0.0, 	# 0,0,26,0
                        0.0, 	# 0,0,26,1
                        0.0, 	# 0,0,26,2
                        0.0, 	# 0,0,26,3
                        0.0, 	# 0,0,26,4
                        0.0, 	# 0,0,26,5
                        0.0, 	# 0,0,26,6
                        0.0, 	# 0,0,26,7
                        0.0, 	# 0,0,26,8
                        0.0, 	# 0,0,26,9
                        0.0, 	# 0,0,26,10
                        0.0, 	# 0,0,26,11
                        0.0, 	# 0,0,26,12
                        0.0, 	# 0,0,26,13
                        0.0, 	# 0,0,26,14
                        0.0, 	# 0,0,26,15
                        0.0, 	# 0,0,26,16
                        0.0, 	# 0,0,26,17
                        0.0, 	# 0,0,26,18
                        0.0, 	# 0,0,26,19
                        0.0, 	# 0,0,26,20
                        0.0, 	# 0,0,26,21
                        0.0, 	# 0,0,26,22
                        0.0, 	# 0,0,26,23
                        0.0, 	# 0,0,26,24
                        0.0, 	# 0,0,26,25
                        0.0, 	# 0,0,26,26
                        0.0, 	# 0,0,26,27
                    ],
                    [
                        0.0, 	# 0,0,27,0
                        0.0, 	# 0,0,27,1
                        0.0, 	# 0,0,27,2
                        0.0, 	# 0,0,27,3
                        0.0, 	# 0,0,27,4
                        0.0, 	# 0,0,27,5
                        0.0, 	# 0,0,27,6
                        0.0, 	# 0,0,27,7
                        0.0, 	# 0,0,27,8
                        0.0, 	# 0,0,27,9
                        0.0, 	# 0,0,27,10
                        0.0, 	# 0,0,27,11
                        0.0, 	# 0,0,27,12
                        0.0, 	# 0,0,27,13
                        0.0, 	# 0,0,27,14
                        0.0, 	# 0,0,27,15
                        0.0, 	# 0,0,27,16
                        0.0, 	# 0,0,27,17
                        0.0, 	# 0,0,27,18
                        0.0, 	# 0,0,27,19
                        0.0, 	# 0,0,27,20
                        0.0, 	# 0,0,27,21
                        0.0, 	# 0,0,27,22
                        0.0, 	# 0,0,27,23
                        0.0, 	# 0,0,27,24
                        0.0, 	# 0,0,27,25
                        0.0, 	# 0,0,27,26
                        0.0, 	# 0,0,27,27
                    ],
                ],
            ],
        ])
    return input_0
