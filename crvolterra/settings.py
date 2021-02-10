BOT_NAME = 'crvolterra'

SPIDER_MODULES = ['crvolterra.spiders']
NEWSPIDER_MODULE = 'crvolterra.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'crvolterra.pipelines.CrvolterraPipeline': 100,

}