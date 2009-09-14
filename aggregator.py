''' Beakr process that queues messages from defined social networks, which pulls at the frequency allowed by that network. A thread
is started for this process and then another thread is started that watches the queue and processes those conversations. A duplication
check is made, conversations are flagged, aggregated, and other metadata is added to the db about that conversation. '''


import models

orm = scoped_session( sessionmaker( bind = engine ) )