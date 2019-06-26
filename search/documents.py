from django_elasticsearch_dsl import DocType, Index
from store.models import Post

post = Index('post')

@post.doc_type
class PostDocument(DocType):
	class Meta:
		model = Post

		fields = [
			'title',
		]