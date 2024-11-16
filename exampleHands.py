# Hands for testing
class ExampleHands:
    not_flush_hand_1 = [
        {"suit": "spades", "rank": "2", "value": 2},    
        {"suit": "spades", "rank": "5", "value": 5},    
        {"suit": "clubs", "rank": "7", "value": 7},    
        {"suit": "clubs", "rank": "9", "value": 9},    
        {"suit": "clubs", "rank": "J", "value": 11},   
        {"suit": "hearts", "rank": "4", "value": 4},   
        {"suit": "hearts", "rank": "A", "value": 14}, 
    ]

    flush_hand_1 = [
        {"suit": "clubs", "rank": "4", "value": 4},    
        {"suit": "clubs", "rank": "6", "value": 6},    
        {"suit": "clubs", "rank": "7", "value": 7},    
        {"suit": "clubs", "rank": "9", "value": 9},    
        {"suit": "clubs", "rank": "J", "value": 11},   
        {"suit": "hearts", "rank": "4", "value": 4},   
        {"suit": "hearts", "rank": "A", "value": 14},  
    ]
    
    Straight_flush_hand_1 = [
        {"suit": "clubs", "rank": "4", "value": 4},    
        {"suit": "clubs", "rank": "5", "value": 5},    
        {"suit": "clubs", "rank": "6", "value": 6},    
        {"suit": "clubs", "rank": "7", "value": 7},    
        {"suit": "clubs", "rank": "8", "value": 8},   
        {"suit": "hearts", "rank": "4", "value": 4},   
        {"suit": "hearts", "rank": "A", "value": 14},  
    ]

    straight_flush_hand_2 = [
        {"suit": "clubs", "rank": "2", "value": 2},    
        {"suit": "clubs", "rank": "3", "value": 3},    
        {"suit": "clubs", "rank": "4", "value": 4},    
        {"suit": "clubs", "rank": "5", "value": 5},    
        {"suit": "clubs", "rank": "A", "value": 14},   
        {"suit": "hearts", "rank": "J", "value": 11},   
        {"suit": "spades", "rank": "10", "value": 10},  
    ]

    straight_flush_hand_3 = [
        {"suit": "clubs", "rank": "2", "value": 2},    
        {"suit": "clubs", "rank": "3", "value": 3},    
        {"suit": "clubs", "rank": "4", "value": 4},    
        {"suit": "clubs", "rank": "5", "value": 5},    
        {"suit": "clubs", "rank": "6", "value": 6},   
        {"suit": "clubs", "rank": "A", "value": 14},   
        {"suit": "spades", "rank": "10", "value": 10},  
    ]

    Royal_flush_hand_1 = [
        {"suit": "hearts", "rank": "10", "value": 10},    
        {"suit": "hearts", "rank": "J", "value": 11},    
        {"suit": "hearts", "rank": "K", "value": 12},    
        {"suit": "hearts", "rank": "Q", "value": 13},    
        {"suit": "hearts", "rank": "A", "value": 14},   
        {"suit": "spades", "rank": "4", "value": 4},   
        {"suit": "spades", "rank": "2", "value": 2},  
    ]

    Four_of_a_kind_1 = [
        {"suit": "diamonds", "rank": "3", "value": 3},    
        {"suit": "spades", "rank": "3", "value": 3},    
        {"suit": "hearts", "rank": "3", "value": 3},    
        {"suit": "clubs", "rank": "3", "value": 3},    
        {"suit": "spades", "rank": "4", "value": 4},   
        {"suit": "hearts", "rank": "7", "value": 7},   
        {"suit": "spades", "rank": "9", "value": 9},  
    ]

    Four_of_a_kind_2 = [
        {"suit": "heart", "rank": "5", "value": 5},    
        {"suit": "hearts", "rank": "8", "value": 8},    
        {"suit": "clubs", "rank": "9", "value": 9},    
        {"suit": "clubs", "rank": "J", "value": 11},    
        {"suit": "hearts", "rank": "J", "value": 11},   
        {"suit": "spades", "rank": "J", "value": 11},   
        {"suit": "diamonds", "rank": "J", "value": 11},  
    ]

    Three_of_a_kind_1 = [
        {"suit": "hearts", "rank": "4", "value": 4},
        {"suit": "clubs", "rank": "7", "value": 7},
        {"suit": "diamonds", "rank": "10", "value": 10},
        {"suit": "spades", "rank": "Q", "value": 12},
        {"suit": "clubs", "rank": "K", "value": 13},
        {"suit": "hearts", "rank": "K", "value": 13},
        {"suit": "diamonds", "rank": "K", "value": 13},
    ]

    two_Three_of_a_kind_1 = [
        {"suit": "hearts", "rank": "2", "value": 2},
        {"suit": "clubs", "rank": "2", "value": 2},
        {"suit": "diamonds", "rank": "2", "value": 2},
        {"suit": "spades", "rank": "J", "value": 11},
        {"suit": "clubs", "rank": "J", "value": 11},
        {"suit": "hearts", "rank": "J", "value": 11},
        {"suit": "diamonds", "rank": "K", "value": 13},
    ]

    Two_of_a_kind_1 = [
        {"suit": "hearts", "rank": "3", "value": 3},
        {"suit": "clubs", "rank": "6", "value": 6},
        {"suit": "diamonds", "rank": "9", "value": 9},
        {"suit": "spades", "rank": "10", "value": 10},
        {"suit": "hearts", "rank": "J", "value": 11},
        {"suit": "spades", "rank": "J", "value": 11},
        {"suit": "diamonds", "rank": "A", "value": 14},
    ]

    Two_pair_1 = [
        {"suit": "hearts", "rank": "2", "value": 2},
        {"suit": "clubs", "rank": "5", "value": 5},
        {"suit": "spades", "rank": "8", "value": 8},
        {"suit": "diamonds", "rank": "8", "value": 8},
        {"suit": "hearts", "rank": "Q", "value": 12},
        {"suit": "clubs", "rank": "Q", "value": 12},
        {"suit": "spades", "rank": "K", "value": 13},
    ]

    full_house_1 = [
        {"suit": "hearts", "rank": "3", "value": 3},
        {"suit": "clubs", "rank": "3", "value": 3},
        {"suit": "spades", "rank": "7", "value": 7},
        {"suit": "diamonds", "rank": "7", "value": 7},
        {"suit": "hearts", "rank": "7", "value": 7},
        {"suit": "clubs", "rank": "9", "value": 9},
        {"suit": "spades", "rank": "10", "value": 10},
    ]

    full_house_2 = [
        {"suit": "hearts", "rank": "2", "value": 2},
        {"suit": "clubs", "rank": "2", "value": 2},
        {"suit": "spades", "rank": "2", "value": 2},
        {"suit": "diamonds", "rank": "4", "value": 4},
        {"suit": "hearts", "rank": "9", "value": 9},
        {"suit": "clubs", "rank": "9", "value": 9},
        {"suit": "spades", "rank": "J", "value": 11},
    ]

    four_of_a_kind_and_two_of_a_kind = [
        {"suit": "hearts", "rank": "2", "value": 4},
        {"suit": "clubs", "rank": "7", "value": 7},
        {"suit": "spades", "rank": "7", "value": 7},
        {"suit": "diamonds", "rank": "9", "value": 9},
        {"suit": "hearts", "rank": "9", "value": 9},
        {"suit": "clubs", "rank": "9", "value": 9},
        {"suit": "spades", "rank": "9", "value": 9},
    ]

    three_two_of_a_kind = [
        {"suit": "hearts", "rank": "3", "value": 3},
        {"suit": "clubs", "rank": "3", "value": 3},
        {"suit": "spades", "rank": "5", "value": 5},
        {"suit": "diamonds", "rank": "5", "value": 5},
        {"suit": "hearts", "rank": "J", "value": 11},
        {"suit": "clubs", "rank": "J", "value": 11},
        {"suit": "spades", "rank": "A", "value": 14},
    ]

    three_of_a_kind_two_two_of_a_kind = [
        {"suit": "hearts", "rank": "4", "value": 4},
        {"suit": "clubs", "rank": "4", "value": 4},
        {"suit": "spades", "rank": "6", "value": 6},
        {"suit": "diamonds", "rank": "6", "value": 6},
        {"suit": "hearts", "rank": "6", "value": 6},
        {"suit": "clubs", "rank": "K", "value": 12},
        {"suit": "spades", "rank": "K", "value": 12},
    ]