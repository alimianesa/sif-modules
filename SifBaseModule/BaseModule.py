import SifBaseModule.BaseDevice as BaseDevice
import SifBaseModule.BasePoint as BasePoint
import SifBaseModule.BaseAction as BaseAction


class BaseModule:
    def __init__(
            self,
            _app,
            _id: int,
            _key: str,
            _title: str,
            _subtitle: str,
            _description: str,
            _version: str,
            _vendor_id: int,
            _vendor_title: str,
            _device: BaseDevice,
            _point: BasePoint,
            _action: BaseAction,
            _path: str,
            _permissions: dict = None,
            _metas: dict = None
    ) -> None:
        self.__app = _app  # app
        self.__id = _id  # Unique Key for any Vendor
        self.__key = _key  # Unique Key for any Vendor
        self.__title = _title
        self.__subtitle = _subtitle
        self.__description = _description
        self.__version = _version
        self.__vendor_uid = _vendor_id
        self.__vendor_title = _vendor_title
        self.__device = _device
        self.__point = _point
        self.__action = _action
        self.__path = _path
        self.__permissions = _permissions
        self.__metas = _metas
        super().__init__()

    @property
    def action(self):
        return self.__action

    @property
    def id(self):
        return self.__id

    @property
    def key(self):
        return self.__key

    @property
    def title(self) -> str:
        return self.__title

    @property
    def subtitle(self):
        return self.__subtitle

    @property
    def description(self):
        return self.__description

    @property
    def version(self):
        return self.__version

    @property
    def vendor_id(self):
        return self.__vendor_uid

    @property
    def vendor_title(self):
        return self.__vendor_title

    @property
    def device(self):
        return self.__device

    @property
    def point(self):
        return self.__point

    @property
    def path(self):
        return self.__path

    @property
    def permissions(self):
        return self.__permissions

    @property
    def metas(self):
        return self.__metas

    @property
    def app(self):
        return self.__app

    def init(self):
        print('init')

    def boot(self):
        print('boot')

    def add_socket(
            self,
            _id: int,
            _type: str,
            _host: str,
            _port: int,
            _callback
    ):
        # TODO Important for various sockets
        self.__app.add_socket(
            _id=_id,
            _type=_type,
            _host=_host,
            _port=_port,
            _module_id=self.__id,
            _callback=_callback
        )
        return self.__app.get_socket(self.__id, _id)

    def get_sockets(self):
        return self.__app.get_sockets(self.__id)

    def get_socket(self, _socket_id: int):
        return self.__app.get_socket(self.__id, _socket_id)
