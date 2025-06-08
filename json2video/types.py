from pydantic import BaseModel, Field
from typing import Optional


class Image(BaseModel):
    type: str = Field(..., description="Type of the element (e.g., image, text)", serialization_alias="type")
    src: str = Field(..., description="Source URL of the element")
    width: int = Field(..., description="Width of the element in pixels")
    height: int = Field(..., description="Height of the element in pixels")
    x: int = Field(..., description="X position of the element in the scene")
    y: int = Field(..., description="Y position of the element in the scene")
    zoom: float = Field(0, description="Zoom level of the element, default is 1.0")
    
  
class Video(BaseModel):
    type: str = Field(..., description="Type of the element (e.g., image, text)", serialization_alias="type")
    src: str = Field(..., description="Source URL of the video element")
    width: Optional[int] = Field(None, description="Width of the video element in pixels")
    height: Optional[int] = Field(None, description="Height of the video element in pixels")
    x: int = Field(..., description="X position of the video element in the scene")
    y: int = Field(..., description="Y position of the video element in the scene")
    position: Optional[str] = Field(None, description="Position of the video element in the scene (e.g., 'top-left', 'center')")
    muted: bool = Field(False, description="Whether the video element is muted, default is False")
    mask: Optional[str] = Field(None, description="Mask settings for the video element, if any")
  
 
class Audio(BaseModel):
    type: str = Field(..., description="Type of the element (e.g., image, text)", serialization_alias="type")
    src: str = Field(..., description="Source URL of the audio element")
    volume: float = Field(1.0, description="Volume level of the audio element, default is 1.0")
    
    
class Subtitles(BaseModel):
    type: str = Field(..., description="Type of the element (e.g., image, text)", serialization_alias="type")
    settings: dict = Field(..., description="Settings for the subtitles element")
    language: str = Field(..., description="Language of the subtitles")
      
    
class Scene(BaseModel):
    elements: list = Field(..., description="List of elements in the scene")
    transition: dict = Field(..., description="Transition effects for the scene")
    duration: int = Field(..., description="Duration of the scene in seconds")
  
    
class Movie(BaseModel):
    resolution: str = Field(..., description="Video resolution")
    quality: str = Field(..., description="Video quality")
    width: int = Field(..., description="Video width in pixels")
    height: int = Field(..., description="Video height in pixels")
    scenes: list[Scene] = Field(..., description="List of scenes in the video")
    elements: list = Field([], description="List of elements in the video, if any")
    
    
class CreateMovieResponse(BaseModel):
    success: bool = Field(..., description="Status of the movie creation process")
    project: str = Field(..., description="ID of the created project")
    timestamp: str = Field(..., description="Timestamp of the movie creation")
