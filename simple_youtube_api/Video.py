from simple_youtube_api import youtube_api


#TODO add variables
class Video(object):
  
    '''
      Super class for YouTubeVideo and LocalVideo
      
      Attributes
     -----------
     
     file_path:
       The file path for the video
     
     title:
      The title for the video on YouTube
     
     description:
       The description for the video on YouTube
     
     tags:
       The list of tags that the video is going to have on YouTube
     
     category:
         The category that the video would be on YouTube
         
     '''

    def __init__(self):
        
        self.title = ""
        self.description = ""
        self.tags = []
        self.category = None
        self.privacy_status = "private"

    def set_title(self, title):
        if len(title) > youtube_api.MAX_YOUTUBE_TITLE_LENGTH:
            print("Title is too long: " + len(title))
        else:
            self.title = title

    def get_title(self):
        return self.title


    def set_description(self, description):
        if len(description) > youtube_api.MAX_YOUTUBE_DESCRIPTION_LENGTH:
            print("Description is too long: " + len(description))
        else:
            self.description = description

    def get_description(self):
        return self.description


    def set_tags(self, tags):
        """
        Sets tags to the video
        """

        if len("".join(tags)) > youtube_api.MAX_YOUTUBE_TAGS_LENGTH:
            print("Description is too long: " + len("".join(tags)))
        else:
            self.tags = tags

    def get_tags(self):
        return self.tags


    def set_category(self, category):
        if category is None:
            category = None
            return

        category = category.lower()
        if category in youtube_api.YOUTUBE_CATEGORIES_ID_LIST:
            self.category = category
        elif category in youtube_api.YOUTUBE_CATEGORIES_DICT.keys():
            self.category = youtube_api.YOUTUBE_CATEGORIES_DICT[category]
        else:
            print("Not a valid category")
            self.category = None

    def get_category(self):
        return self.category


    def set_privacy_status(self, privacy_status):

        if privacy_status not in youtube_api.VALID_PRIVACY_STATUSES:
            print("Not a valid privacy status: " + privacy_status)
        else:
            self.privacy_status = privacy_status

    def get_privacy_status(self):
        return self.privacy_status

