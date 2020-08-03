from celery import shared_task
from crawler.models import Link, Keyword, Category, UserProfile, CrawledLinks
from scheduler.models import ScrapedLink
from django.contrib.auth.models import User

@shared_task
def save_models(query, cat, link, scrape_data, reschedule, username):
    no_of_links = 0
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    keyword = Keyword.objects.get(name=query)
    category = Category.objects.get(name=cat)
    scraped_link = ScrapedLink.objects.get_or_create(link=link, scrape_data=scrape_data,
                                                     schedule_day=reschedule)[0]
    scraped_link.save()

    link = Link.objects.get_or_create(keyword=keyword, category=category, link=link, scrape_data=scrape_data)[0]
    link.save()

    profile_update, created = CrawledLinks.objects.get_or_create(userprofile=userprofile,
                                                                 link=link, reschedule=reschedule)
    profile_update.save()

    if created:
        no_of_links += 1

    userprofile.crawled_links += no_of_links
    userprofile.save()

