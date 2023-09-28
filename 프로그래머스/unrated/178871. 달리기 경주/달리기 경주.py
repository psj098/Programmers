def solution(players, callings):
    
    position = {player: idx for idx, player in enumerate(players)}
    
    for calling in callings: 
        idx = position[calling] 
        players[idx], players[idx-1] = players[idx-1], players[idx] 
        
        position[players[idx]] = idx 
        position[players[idx-1]] = idx - 1
    
    return players
