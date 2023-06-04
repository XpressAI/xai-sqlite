from xai_components.base import InArg, OutArg, InCompArg, Component, BaseComponent, xai_component
import sqlite3


@xai_component
class SqliteOpenDB(Component):
    file_name: InCompArg[str]
    
    def execute(self, ctx):
        def get_db():
            db = sqlite3.connect(self.file_name.value)
            db.row_factory = sqlite3.Row
            return db
        
        ctx['sqlite_get_db'] = get_db


@xai_component
class SqliteWithTransaction(Component):
    in_transaction: BaseComponent
    
    def execute(self, ctx):
        db = ctx['sqlite_get_db']()
        with db:
            ctx['sqlite_db'] = db
            next = self.in_transaction
            while next:
                next = next.do(ctx)
        db.close()
        ctx['sqlite_db'] = None


@xai_component
class SqliteExecute(Component):
    query: InCompArg[str]
    args: InArg[list]
    
    def execute(self, ctx):
        db = ctx['sqlite_db']
        
        if self.args.value is None:
            db.execute(self.query.value)
        else:
            db.execute(self.query.value, tuple(self.args.value))


@xai_component
class SqliteExecuteScript(Component):
    file_path: InCompArg[str]
    
    def execute(self, ctx):
        db = ctx['sqlite_db']
        
        with app.open_resource(self.file_path.value, mode='r') as f:
            db.cursor().executescript(f.read())


@xai_component
class SqliteFetchOne(Component):
    query: InCompArg[str]
    args: InArg[list]
    result: OutArg[dict]
    
    def execute(self, ctx):
        db = ctx['sqlite_db']
        
        if self.args.value is None:
            self.result.value = db.execute(self.query.value).fetchone()
        else:
            self.result.value = db.execute(self.query.value, tuple(self.args.value)).fetchone()


@xai_component
class SqliteFetchAll(Component):
    query: InCompArg[str]
    args: InArg[list]
    result: OutArg[list]
    
    def execute(self, ctx):
        db = ctx['sqlite_db']
        
        if self.args.value is None:
            self.result.value = db.execute(self.query.value).fetchall()
        else:
            self.result.value = db.execute(self.query.value, tuple(self.args.value)).fetchall()