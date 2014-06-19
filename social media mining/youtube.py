import gdata.youtube
import gdata.youtube.service


def GetEntryDetails(entry):
    return {
        'Video title': entry.media.title.text,
        'Video published on': entry.published.text,
        'Video category': entry.media.category[0].text,
        'Video watch page': entry.media.player.url,
        'Video duration': entry.media.duration.seconds,
        'Video view count': entry.statistics.view_count,
        'Video rating': entry.rating.average,
        'thumbnail': entry.media.thumbnail[0].url,
    }


def GetVideoFeed(feed):
  return [GetEntryDetails(entry) for entry in feed.entry]


def GetFeedByUrl(uri):
  yt_service = gdata.youtube.service.YouTubeService()

  # You can retrieve a YouTubeVideoFeed by passing in the URI
  return GetVideoFeed(yt_service.GetYouTubeVideoFeed(uri))

