class SquareField():
    def __init__(self, len, final_states):
        self.len = len
        self.final_states = final_states

        self.current_pos = (0,0)

    def reset(self):
        self.current_pos = (0,0)
        return self.current_pos
    
    def step(self, action):
        l,r = self.current_pos

        if action==0:
            if l<self.len-1:
                l = (l+1)%self.len
        elif action==1:
            if l>0: 
                l = (l-1)%self.len
        elif action==2:
            if r>0:
                r = (r-1)%self.len
        elif action==3:
            if r<self.len-1:
                r = (r+1)%self.len
        else:
            raise ValueError

        self.current_pos = (l,r)
        if (l,r) in self.final_states:
            obs = (l,r)
            reward = self.final_states[(l,r)]
            done = True
            info = {}
            return obs, reward, done, info
        else:
            return (l,r), 0, False, {}    