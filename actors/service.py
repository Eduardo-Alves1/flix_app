import streamlit as st
from actors.repository import ActorsRepository

class ActorService():
    def __init__(self):
        self.actor_repository = ActorsRepository()

    def get_actors(self):
        return self.actor_repository.get_actors()
    
    def create_actors(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        return self.actor_repository.create_actor(actor)
    

# def get_actors(self):
#         if 'actors' in st.session_state:
#             return st.session_state.actors
#         actors = self.actor_repository.get_actors()
#         return actors
    
#     def create_actors(self, name, birthday, nationality):
#         actor = dict(
#             name=name,
#             birthday=birthday,
#             nationality=nationality,
#         )
#         new_actor = self.actor_repository.create_actor(actor)
#         st.session_state.actors.append(new_actor)
#         return new_actor